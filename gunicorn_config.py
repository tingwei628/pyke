from pathlib import Path
bind = 'unix:///tmp/nginx.socket'
def pre_fork(server, worker):
    Path('/tmp/app-initialized').touch()
