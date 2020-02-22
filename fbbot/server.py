from flask import Flask
from config import Config

"""
fbbot is the variable name of Flask app
"""
fbbot = Flask(__name__) 
""" __name__ : executed module name""" 
fbbot.config.from_object(Config)


@fbbot.route('/')
def index():
    return 'I am fbbot'

@fbbot.route('anywhere')
def anywhere():
    return 'anywhere'



if __name__ == '__main__': 
    fbbot.run()
