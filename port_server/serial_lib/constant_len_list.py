
class constant_len_list :
    def __init__(self,num=120):
        self.num = num ;
        self.l = list();
    
    def add_tail(self,s):
        self.l.append(s);
        if len(self.l) > self.num and self.num > 0 :
            self.l = self.l[len(self.l)-self.num:]
     
    def get_data(self):
        return self.l ;
        
    def __str__(self):
        return str(self.l);

        
        
if __name__ == '__main__':
    print "test begin."    
    c = constant_len_list() ;
    for i in range(1000):
        c.add_tail(i);
    print str(c);
    print len(c.l)
    print "test end"
