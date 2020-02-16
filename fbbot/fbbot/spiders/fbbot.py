from fbbot.items import FbbotItem as PostItem
import scrapy
import time

"""SN = Software News
"""
class SNSpider(scrapy.Spider):
    name = 'SNbot'
    start_urls = ['https://mbasic.facebook.com/軟體每日新聞-102888707949836/']

    def parse(self, response):
        url = 'https://mbasic.facebook.com/軟體每日新聞-102888707949836/'
        yield scrapy.Request(url, callback=self.parse_post)
        
        """
        if next_page_url is not None:
            yield scrapy.Request(next_page_url, callback=self.parse_post)
        """


    def parse_post(self, response):
        post = PostItem()
        for index in range(1,6):
            try:
                tag = response.css('#u_0_{0}'.format(index))
                post['date'] = tag.xpath('//[@class="gf"]')
                # post['text'] = tag.xpath('//div')
                # post['link'] = tag.xpath('//div')
                print("post ", post)
                yield post

            except IndexError:
                pass
                continue
    
