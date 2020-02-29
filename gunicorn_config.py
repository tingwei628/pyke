bind = 'unix:///tmp/nginx.socket'
def when_ready(server):
    open('/tmp/app-initialized').close()
