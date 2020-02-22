- runtime.txt // description of python runtim
- requirements.txt // description of python packages
- Procfile // for heroku to run python server

In Procfile

```
web gunicorn [your_app_file_name]:[your_app_name]

for example, web gunicorn server:fbbot
app filename is server.py
variable name of Flask in app file is fbbot

```


- gunicorn // for heroku 

