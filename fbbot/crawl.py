from requests_html import AsyncHTMLSession
from secrets import choice 
from bs4 import BeautifulSoup as bs4
from datetime import datetime
from time import(
    sleep
)
from flask import request
import os
import re
import asyncio
import threading
import pyppeteer


http_proxies = []
https_proxies = []
all_lines = []
current_dir=os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(current_dir, 'doc/proxy.txt'), 'r') as f:
    all_lines=f.readlines()

https_proxies = all_lines[1:2]
http_proxies = all_lines[3:4]

def getposts():
    new_loop=asyncio.new_event_loop()
    asyncio.set_event_loop(new_loop)   
    session = AsyncHTMLSession()
    return session.run(getposts_async)
async def getposts_async():
    htmls = []
    base_url = 'https://mbasic.facebook.com'
    base_page_url = 'https://mbasic.facebook.com/%E8%BB%9F%E9%AB%94%E6%AF%8F%E6%97%A5%E6%96%B0%E8%81%9E-102888707949836/' 
    urls = []
    next_page_url=base_page_url
    
    """
    collect urls
    """

    regex_story = re.compile(r'^/story\.php.*=%2As-R$')
    regex_next_page = re.compile(r'^/profile\.php\?sectionLoadingID.*$')
    session = AsyncHTMLSession()
    browser = await pyppeteer.launch({'ignoreHTTPSErrors':True, 'headless':True, 'handleSIGINT':False, 'handleSIGTERM':False, 'handleSIGHUP':False, 'args': ['--no-sandbox', '--disable-setuid-sandbox']})    
    session._browser = browser
    cookies_str=os.environ.get('COOKIES_STR')
    cookie_dict={}
    for kv_pair in cookies_str.split('; '):
        kv = kv_pair.split('=')
        cookie_dict[kv[0]]=kv[1]
    
    while True:
      resp_page = await session.get(next_page_url, cookies=cookie_dict)
      resp_page.encoding = 'utf-8'
      #await resp_page.html.arender()
      soup_page = resp_page.html.links
      url_tags = [link for link in soup_page if regex_story.search(link)]
      next_page_tags = [link for link in soup_page if regex_next_page.search(link)]
      
      for url_tag in url_tags:
          urls.append('{base_url}{href}'.format(base_url=base_url, href=url_tag))
      next_page_url = None if len(next_page_tags)== 0 else '{base_url}{href}'.format(base_url=base_url, href=next_page_tags[0])
      #print('next_page_url ', next_page_url)
      if(next_page_url is None):
          break
      
    
    #print('urls ', urls)

    """
    collect data
    """
    posts=[]
    for url in urls:
        #httpproxy=choice(http_proxies)
        #httpsproxy=choice(https_proxies)
        resp = await session.get(url, cookies=cookie_dict)
        #print('host ', request.environ['REMOTE_ADDR'])
        resp.encoding = 'utf-8'
        #htmls.append(resp.html)
        posts.append({ 'title':'','url':'','content': resp.html.find('div.bc')[0].text})
        """sleep for 5 sec
        """
        # time.sleep(5) 
    #print(htmls)
    #posts=[{'title': '123','url': 'okok','content':'okkk'}, {'title': '222', 'url': '222', 'content': '555'}]   
    return posts
