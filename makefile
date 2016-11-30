
run :
	python falcon_cli/host_counting.py &
	uwsgi runserver.ini &
	#uwsgi -s 127.0.0.1:9092 -p 8 --daemonize /var/log/uwsgi.log -w app_site.wsgi  >> log &
memcached :
	memcached -d -m 128 -u root  -p 11212  -P /tmp/memcached.pid
kill_all:
	pgrep uwsgi | xargs kill -9
	pgrep python | xargs kill -9
