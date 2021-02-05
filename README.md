# pybot
A bot in python


> These files need to be at root of the project for deploying on Heroku 

- runtime.txt // description of python runtim
- requirements.txt // description of python packages
- Procfile // for heroku to run python server

In Procfile

```
web gunicorn -b:$PORT --pythonpath [app_directory]  [your_app_file_name]:[your_variable_name_of_flask_app]

for example, web gunicorn server:fbbot
app filename is server.py
variable name of Flask app file is fbbot

```


- gunicorn // for heroku

## Install
```
python setup.py install
```
