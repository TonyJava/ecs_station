import sys, glob

sys.path.append('gen-py')
sys.path.insert(0, glob.glob('./lib/py/build/lib.*')[0])

from port_server import port_server
from port_server.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol



try:

    # Make socket
    transport = TSocket.TSocket("localhost", 9090) ;
    # Buffering is critical. Raw sockets are very slow
    transport = TTransport.TFramedTransport(transport)

    # Wrap in a protocol
    protocol = TBinaryProtocol.TBinaryProtocol(transport)

    # Create a client to use the protocol encoder
    client = port_server.Client(protocol)

    # Connect!
    transport.open()

    cmd = "test" ;

    res = client.exc(cmd);
    print res 
except e:
    print str(e);
    
    