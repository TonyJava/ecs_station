import os,time ;

def check_pid_file(pidfile,cmd):
    pf = open(pidfile);
    pid = int(pf.read());
    print pid ;
    try:
        os.kill(pid,0);
    except OSError :
        print "pid is not running"
        os.popen(cmd+"&");
    return True ;



if __name__ == "__main__":
    print "monitor start"
    while True :
        check_pid_file("/tmp/PythonServer.pid","cd ~/source/ecs_station/port_server;python server.py");
        time.sleep(5)


