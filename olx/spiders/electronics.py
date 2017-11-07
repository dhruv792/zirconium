# -*- coding: utf-8 -*-
import pymongo
from pymongo import MongoClient
import sys
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from olx.items import OlxItem
import json
from bs4 import BeautifulSoup
class ElectronicsSpider(CrawlSpider):
    
    
    name = "electronics"
    allowed_domains = ["https://www.99acres.com"]
    start_urls = [
        "https://www.99acres.com/property-in-mumbai-ffid"
    ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pgselActive',)),
             callback="parse",
             follow=True),)

    # def start_requests(self):
    #     urls = [
    #         'https://www.99acres.com/property-in-mumbai-ffid',
    #         # 'http://quotes.toscrape.com/page/2/',
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        client = MongoClient('52.66.174.199', 27017)
        zirconium = client.zirconium
        properties = zirconium.properties
        propertiesArray = []
        soup = BeautifulSoup(response.body, 'lxml')
        for tag in soup.findAll('div',{'class':'srpttl'}):
            x = tag.find('span')
            # print(x)
            y  = x.find_all('b')
            try:
                item = {
                    'price':  y[1].string,
                    'description': tag.a.string,
                    'link': "https://www.99acres.com"+tag.a['href']
                }

                propertiesArray.append(item)
                # print(tag)
                # try:
                #     print(y[1].string)
            except Exception:
                continue
            # print(tag.a.string)
            # print(tag.a['href'])
            
            # break
        # print((propertiesArray))
        result = properties.insert(propertiesArray)
        print("result", result)
            
            # for x in tag.span.find_all('b'):
            #     print(x.string)
        # x = soup.find_all('.wrapttl')
        # print(x)
        # item_links = soup.css('.wrapttl').extract()
        # print(len(item_links))
        # data = {}
        # data['asds'] = item_links
        # data = b'123'
        # # return
        # page = response.url.split("/")[-2]
        # print(soup.)
        # filename = 'quotes22223.html'
        # with open(filename, 'w') as f:
        #     f.write(str(soup))
        # self.log('Saved file %s' % filename)

    # def parse_item(self, response):
    #     print('Processing..')
    #     item_links = response.css('.wrapttl > .srpttl > a::attr(href)').extract()
    #     # print (item_links)
    #     # return item_links
    #     for a in item_links:
    #         yield scrapy.Request(a, callback=self.parse_detail_page)

    # def parse_detail_page(self, response):
    #     print('Processing1..' + response.url)
        # title = response.css('h1::text').extract()[0].strip()
        # price = response.css('.pricelabel > strong::text').extract()[0]
        # item = OlxItem()
        # item['title'] = title
        # item['price'] = price
        # item['url'] = response.url
        # yield item
