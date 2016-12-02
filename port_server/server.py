
import sys, glob,os ;
import commands,json ;
import urllib2 ;
 
sys.path.append('./gen-py') 
sys.path.append('./serial_lib') 
#sys.path.insert(0, glob.glob('./lib/py/build/lib.*')[0])

from port_server import port_server
from port_server.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server import TNonblockingServer

from serial_manager import * ;

class port_server_handler:
    def __init__(self):
        self.sm = serial_manager(port="/dev/ttyUSB0");
        self.sm.start();
        

    def exc(self,cmd):
        try:
            res = os.popen(cmd).read();
        except Exception as e :
            res = str(e) ;
        return res;
    
    def exc_without_return(self,cmd) :
        try:
            res = os.popen(cmd).read();
        except :
            pass ;
    
    def set_serial_port(self,port,rate):
        rtn = self.sm.set_serial_port(port,rate) ; 
        return json.dumps({"code":0,"result":rtn});
    
    def send_cmd(self,code):
        self.sm.send_command(code);
    
    def get_var(self,key):
        res= {} ;
        try:
            val = self.sm.get_value(key);
            res = {"code":0,"result":val} ;
        except Exception as e :
            res = {"code":1,"result":e};
        return json.dumps(res);

    def get_var_table(self,key):
        res = {};
        try:
            rtn = self.sm.get_var_table()
            res = {"code":0,"result":rtn};
        except Exception as e :
            res = {"code":1,"result":e};
        return json.dumps(res);

    def get_var_list(self,key):
        res = {} ;
        try:
            rtn = self.sm.get_var_list(key);
            res = {"code":0,"result":rtn};
        except Exception as e :
            res = {"code":1,"result":e};
        return json.dumps(res);
    
    def set_list_len(self,len):
        res = {} ;
        try:
            self.sm.set_cache_size(len);
            res = {"code":0,"result":"ok"};
        except Exception as e :
            res = {"code":1,"result":e};
        return json.dumps(res); 



if __name__ == '__main__':
    print "Server start."
    handler = port_server_handler()
    processor = port_server.Processor(handler)
    transport = TSocket.TServerSocket(port=9090)
    tfactory = TTransport.TFramedTransportFactory()
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)
    #server = TNonblockingServer.TNonblockingServer(processor, transport)

    # You could do one of these for a multithreaded server
    #server = TServer.TThreadedServer(processor, transport, tfactory, pfactory)
    #server = TServer.TThreadPoolServer(processor, transport, tfactory, pfactory)

    # pid = str(os.getpid())
    # PIDFILE = '/tmp/PythonServer.pid'
    # pidfile = open(PIDFILE,'w')
    # pidfile.write(pid)
    # pidfile.close()

    print 'Starting the server...'
    server.serve()
    print 'done.'
