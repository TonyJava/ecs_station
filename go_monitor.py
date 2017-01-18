
import time ;
from go import * ;


if __name__ == "main":
    pid = str(os.getpid())
    PIDFILE = '/tmp/go_monitor.pid'
    pidfile = open(PIDFILE,'w')
    pidfile.write(pid)
    pidfile.close()

    print "monitor start"
    while True :
        check_pid_file("/tmp/go.pid","cd ~/source/ecs_station;python go.py");
        time.sleep(5)
