from flask import Flask
from config import Config
import os


"""
fbbot is the variable name of Flask app
"""
fbbot = Flask(__name__) 
""" __name__ : executed module name""" 
fbbot.config.from_object(Config)


@fbbot.route('/')
def index():
    return 'I am fbbot'

@fbbot.route('/anywhere')
def anywhere():
    return 'anywhere'

"""
default 5000
"""
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__': 
    fbbot.run(host='0.0.0.0', port=port)
