import httplib,urllib,random,json,string ;


class ecs_http_client:
    host = "127.0.0.1:8000"
    def list_command(self,host = None):
        if host == None :
            host = self.host ; 
        resp = requests.get(host+"/station/list_command/");
        return json.loads(resp.text) 

    def insert_command(self,host=None,key,code):
        if host == None :
            host = self.host ; 
        resp = requests.get(host+"/station/insert_command/",data = json.dumps({"key":str(key),"code":str(code)}));
        return json.loads(resp.text)
    
    def delete_command(self,host=None,key=None):
        if host == None :
            host = self.host ; 
        if key == None :
            resp = requests.get(host+"/station/delete_command/",data=json.dumps([str(key)]));
        else :
            resp = requests.get(host+"/station/delete_command/");
        return json.loads(resp.text) 

if __name__ == '__main__':
    print "test"
    e_test = ecs_http_client();
    print e_test.list_command();
    print e_test.insert_command(key="test1",code="code1");
    print e_test.delete_command();