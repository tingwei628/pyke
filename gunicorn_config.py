from pathlib import Path
pythonpath='fbbot'
preload_app=True
bind = 'unix:///tmp/nginx.socket'
#def pre_fork(server, worker):
#    Path('/tmp/app-initialized').touch()
