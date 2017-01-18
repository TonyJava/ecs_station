import os,time ;

def check_pid_file(pidfile,cmd):
    try:
        pf = open(pidfile);
        pid = int(pf.read());
        print pid ;
    except IOError:
        print "pidfile can not be found"
        os.popen(cmd+"&");
    try:
        os.kill(pid,0);
    except OSError :
        print "pid is not running"
        os.popen(cmd+"&");
    return pid ;



if __name__ == "__main__":
    pid = str(os.getpid())
    PIDFILE = '/tmp/go.pid'
    pidfile = open(PIDFILE,'w')
    pidfile.write(pid)
    pidfile.close()

    print "monitor start"
    while True :
        check_pid_file("/tmp/PythonServer.pid","cd ~/source/ecs_station/port_server;python server.py");
        check_pid_file("/tmp/ui_process.pid","cd ~/source/ecs_station/RASPERY_UI;python3 main.py");
        check_pid_file("/tmp/go_monitor.pid","cd ~/source/ecs_station;python go_monitor.py");
        time.sleep(5)


