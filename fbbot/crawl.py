import requests
from secrets import choice 
from bs4 import BeautifulSoup
from datetime import datetime
from time import(
    sleep
)
from flask import request
import os

http_proxies = []
https_proxies = []
all_lines = []

with open(os.path.join(os.getcwd(), 'doc/proxy.txt'), 'r') as f:
    all_lines=f.readlines()

https_proxies = all_lines[1:2]
http_proxies = all_lines[3:4]

def getposts():
    htmls = []
    urls = ['https://mbasic.facebook.com/%E8%BB%9F%E9%AB%94%E6%AF%8F%E6%97%A5%E6%96%B0%E8%81%9E-102888707949836/']
    
    for url in urls:
        httpproxy=choice(http_proxies)
        httpsproxy=choice(https_proxies)
        resp = requests.get(url, stream=True)
        print('host ', request.environ['REMOTE_ADDR'])
        resp.encoding = 'utf-8'
        htmls.append(resp.text)
        """sleep for 5 sec
        """
        # time.sleep(5) 

    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
    # print (soup.prettify())
    # print(soup.get_text())
        date_tag = soup.select('div.gf')
       
        for tag in date_tag:
            print(tag)
    
    
    posts=[{

            'title': '123',
            'url': 'okok',
            'time': datetime(2020, 2, 21).timetuple(),
            'content':'okkk'
    }]   
    return posts

