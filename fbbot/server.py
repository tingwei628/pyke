from flask import (
        Flask, 
        Blueprint, 
        request, 
        jsonify, 
        render_template, 
        redirect, 
        url_for
)
from config import Config
# from config import Config, ProdConfig
import os
from template_filter import date



"""
strftime // datetime format to str
strptime // str to datetime
"""

from time import (
    strftime, 
    strptime  
)
from datetime import (
    datetime
)

from crawl import (
    getposts
)
# import asyncio
import threading



"""
fbbot is the variable name of Flask app
template_folder = '.' // current_directory
static_folder = '.' // current_directory

"""
fbbot = Flask( __name__,
        static_url_path='',
        static_folder='./assets',
        template_folder='./assets/template')

""" __name__ : executed module name""" 
fbbot.config.from_object(Config)
fbbot.add_template_filter(date
        )


@fbbot.route('/')
def index():    
    # print('index() thread %s' % threading.current_thread().name)
    #return render_template('index.html', post_list=getposts())
    post_list=getposts()
    return 'I am fbbot'

@fbbot.route('/test_redirect')
def test_redirect():
        return redirect(url_for('index'))

"""
@fbbot.route('/test/<string:test_paras>')
def test(test_paras):
    return test_paras
"""
@fbbot.route('/anywhere',methods=['GET'])
def aywhere():
    if 'wtf' == request.args['for']:
        return jsonify('wtf you')
    else:
        return jsonify('fuxx')

"""
default 5000
"""
port = int(os.environ.get('PORT', 5000))

if __name__ == '__main__': 
    fbbot.run(host='0.0.0.0', port=port)
