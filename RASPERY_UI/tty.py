#!/usr/bin/env python
# -*-coding:utf-8-*-

import serial
from time import sleep
import json
import threading
import tools,sys
from Crypto.Cipher import AES
from binascii import a2b_hex

sys.path.append("../port_server/gen-py");
sys.path.append("../port_server/gen-py/port_server");

from port_server import port_server
from port_server.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

class CustomSerial(threading.Thread):
    '''自定义串口类'''
    def __init__(self, com, baud, root, context):
        threading.Thread.__init__(self)
        #self.s = serial.Serial(com, baud)
        self.s = serial.Serial();
        self.root = root
        self.context = context
        self.pointData = {}
        self.seriesData = {}
        self._hyPower = []
        self._liPower = []
        self._allPower = []
        self.x = []
        self.isRun = True
        self._x = 0
        self.key = '1234567890abcdef'
        self._d  = AES.new(self.key, AES.MODE_ECB, b'0' * 16)

    def connect_server(self):
        conn = False ;
        while conn == False :
            try:
                transport = TSocket.TSocket("localhost", 9090) ;
                # Buffering is critical. Raw sockets are very slow
                transport = TTransport.TFramedTransport(transport)
                # Wrap in a protocol
                protocol = TBinaryProtocol.TBinaryProtocol(transport)
                # Create a client to use the protocol encoder
                client = port_server.Client(protocol)
                # Connect!
                transport.open()
                conn = True ;
            except Exception as e :
                print(e)
                client = None ;
        return client

    def run(self):
        #client = self.connect_server();
        err = True ;
        while(self.isRun):
            try:
                if err == True or client == None :
                    client = self.connect_server();
                    if client != None :
                        err = False ;
                    else :
                        continue ;
                j = json.loads(client.get_var_table());     
                if j["code"] == 0 :
                    j = j["result"];
                else :
                    continue ;
                #print(j)          
                power = j["LiVolt"] * j["TotalCurrent"];
                hyPower = j['HyVolt'] * j['DCInCurrent'];
                # print(hyPower)
                self.pointData = {"HyTemp":j["HyTemp"],
                                  #"HyPress":29.22,
                                  "HyPress":j["HyPress"],
                                  "LiVolt":j["LiVolt"],
                                  "HyVolt":j["HyVolt"],
                                  "LiPower":power - hyPower if power > hyPower else 0,
                                  "HyPower":hyPower}
                if self.root.property('isGraphPaint') and not self.root.property('isGraphPause'):
                    self._x += 1                  
                    self._hyPower.append(hyPower)
                    self._liPower.append(power - hyPower)
                    self._allPower.append(power)
                    self.seriesData = {"HyPower":self._hyPower[-300:],
                                       "LiPower":self._liPower[-300:],
                                       "AllPower":self._allPower[-300:],
                                       "x":list(range(self._x))[-300:]}
                sleep(1)

            except Exception as e:
                #print(e)
                err = True ;
                pass


if __name__ == "__main__":
    s = CustomSerial("COM7", 115200)
    s.start()
    while(True):
        print(s.seriesData)
        print(s.pointData)
        sleep(1)
        s.s.close()
