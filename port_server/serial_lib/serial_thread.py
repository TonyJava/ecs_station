
import serial,re
import serial.tools.list_ports
import thread,threading ;
import Queue,time ;

class serial_listen_thread(threading.Thread):
    def __init__(self,port='/dev/cu.usbserial',rate=115200):
        threading.Thread.__init__(self);
        self.port = port ;
        self.rate = rate ;
        #self.serial_port = serial.Serial(port,rate);
        #self.serial_port.open();
        #self.serial_port.timeout = 0.5
        self.running = False ;
        self.recv_queue = Queue.Queue();
        #self.send_queue = Queue.Queue(maxsize=1);
       
    
    def run(self):
        self.running = True ;
        self.__open_port__();
        thread.start_new_thread(self.__rece_thread__,());
        # thread.start_new_thread(self.send_thread,());
    
    def set_serial_port(self,port,rate):
        res = False ;
        if isinstance(port,str) and isinstance(rate,int) : 
            self.port = port ;
            self.rate = rate ;
            self.__open_port__();
            res = True ;
        return res ;
        
    def __open_port__(self):
        if hasattr(self,'serial_port') and self.serial_port.isOpen() :
            self.serial_port.close();
        self.serial_port = serial.Serial(port,rate);
        self.serial_port.open();
        self.serial_port.timeout = 0.5;
            
    def __rece_thread__(self):
        while self.running:
            try:
                self.recv_queue.put(self.serial_port.readline());
            except Exception as identifier:
                print str(identifier);
                time.sleep(1);
                try:
                    self.serial_port = serial.Serial(self.port,self.rate);
                    self.__open_port__();
                except:
                    pass;
            
                
    def send(self,code):
        res = '';
        # while self.recv_queue.qsize > 1 :
        #     res += self.recv_queue.get();
        try :
            self.serial_port.write(code);
        except Exception as e :
            res = e.message ;
        return res ;
      
if __name__ == '__main__':
    print "test begin."
    #ps = serial.tools.list_ports.comports();    
    sth =  serial_listen_thread();
    sth.start();
    
    print sth.send("\x11")
    print "test1"
    print sth.send("\x13")
    print "test2"
    print sth.send("\x15")
    print "test3"
    time.sleep(10);
    
    print "test end."