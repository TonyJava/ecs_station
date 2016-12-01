from serial_thread import *;
import time,json ;
import Queue,thread,threading ;
from constant_len_list import * ;

class serial_manager(threading.Thread):
    
    def __init__(self,port='/dev/cu.usbserial',rate=115200,cache_size=240):
        threading.Thread.__init__(self);
        self.cache_size = cache_size ;
        self.sth = serial_listen_thread(port,rate);
        self.sth.start();
        self.cache = {};
        self.cache_list = {} ;
        self.cmd_queue = Queue.Queue();
        self.running = False ;
       
    def set_cache_size(self,cache_size):
        self.cache_size = cache_size ;

    def get_serial_value(self,key):
        v = None ;
        if serial_manager.cmd_map.has_key(key):
            v=serial_manager.cmd_map[key];
        elif serial_manager.VALUE_MAP.has_key(key):
            v= serial_manager.VALUE_MAP[key];
        if v != None :
            return self.sth.send(v) ;
        else :
            return 0 ;
    
    def run(self):
        self.running = True ;
        thread.start_new_thread(self.__refresh_cache__,());
        thread.start_new_thread(self.__refresh_list__,());
    
    def stop(self):
        self.running = False ;
        
    def __refresh_cache__(self):
        while self.running == True :
            try:
                rtn = self.sth.recv_queue.get();
                var_table = json.loads(rtn);
                for var in var_table :
                    self.cache[var] = var_table[var] ;
            except Exception as e:
                print str(e);
            time.sleep(0.01)         
    
    def get_value(self,key):
        if self.cache.has_key(key) :
            return self.cache[key];
        else :
            return 0 ;
     
    def set_command(self,cmd):
        if cmd in serial_manager.cmd_map :
            self.cmd_queue.put(cmd) ;
            
    def __refresh_list__(self):
        start_time = time.time();
        cnt = 0 ;
        while self.running == True :
            time.sleep(0.1);
            if time.time() > start_time + cnt :
                cnt = cnt + 1 ;
                for key in self.cache :
                    if not self.cache_list.has_key(key) :
                        self.cache_list[key] = constant_len_list(self.cache_size);
                    else :
                        self.cache_list[key].num = self.cache_size ;
                    self.cache_list[key].add_tail(self.get_value(key));



if __name__ == '__main__':
    print "test begin."                    
    sm = serial_manager();
    sm.start();
    for i in range(100):
        time.sleep(10);
        for key in sm.cache_list :
            print str(key),str(sm.cache_list[key])
        print i