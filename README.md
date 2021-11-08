# pyke
> Keyword Extraction in Python

use `Tf-idf` to extract keyword ,then analyze upvotes and comments on Hacker News

---

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

## Reference
https://testdriven.io/blog/fastapi-machine-learning/ \
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/
