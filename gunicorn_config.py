bind = 'unix:///tmp/nginx.socket'
def pre_fork(server, worker):
    open('/tmp/app-initialized', 'w').close()
