import requests
from bs4 import BeautifulSoup



url = 'https://mbasic.facebook.com/%E8%BB%9F%E9%AB%94%E6%AF%8F%E6%97%A5%E6%96%B0%E8%81%9E-102888707949836/'
resp = requests.get(url)

resp.encoding = 'utf-8'

html = resp.text
soup = BeautifulSoup(html, 'html.parser')
# print (soup.prettify())
# print(soup.get_text())
date_tag = soup.select('div.gf')
for tag in date_tag:
    print(tag)


