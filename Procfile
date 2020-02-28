web: bin/start-nginx bundle exec gunicorn --preload -b 'unix:///tmp/nginx.socket':$PORT --pythonpath fbbot server:fbbot
