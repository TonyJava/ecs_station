
import sys, glob,os 
import commands,json 
import urllib2 
 
sys.path.append('gen-py') 
#sys.path.insert(0, glob.glob('./lib/py/build/lib.*')[0])

from port_server import port_server
from port_server.ttypes import *

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.server import TNonblockingServer

class port_server_handler:
    def __init__(self):
        pass ;
        

    def exc(self,cmd):
        print 'exec'
        return "done"
       
    def get_value(self,key):
        print "get_value"
        return "";



if __name__ == '__main__':
    print "test begin."
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
