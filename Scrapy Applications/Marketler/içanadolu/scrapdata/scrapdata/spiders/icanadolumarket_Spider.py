# -*- coding: utf-8 -*-
__author__ = 'AS'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class tripadvisorSpider(CrawlSpider):
    name = "iamarket"
    DOWNLOAD_DELAY = 1
    allowed_domains = ["http://iyifirma.com/"]
    start_urls = ["http://iyifirma.com/firmalar/market/ic-anadolu/"
    ]
    def my_range(start, end, step):
        while start <= end:
            yield start
            start += step

    for i in range(39):
        start_urls.append('http://iyifirma.com/firmalar/market/ic-anadolu/'+str(i)+'/')

    rules = [Rule(LinkExtractor(allow=['/'],deny = ['/firmalar/market/ic-anadolu/','/firmalar/market','iyifirma.com/','http://iyifirma.com/firmalar/market/ic-anadolu/\d+']), 'parse_page')]

    def parse_page(self, response):

        item = items.AkdenizrestorantscrapItem()
        item['isim'] = response.xpath('//*[@id="item-details"]/div[1]/h1/text()')[0].extract()
        item['adres'] = response.xpath('//*[@id="address"]/span[1]/text()')[0].extract()
        item['sehir'] = response.xpath('//*[@id="location"]/a[3]/text()')[0].extract()

        alankodu = response.xpath('//*[@id="item-details"]/div[1]/p[1]/span/a/span/text()')[0].extract()
        numara = response.xpath('//*[@id="item-details"]/div[1]/p[1]/span/a/text()/text()')[0].extract()
        item['tel'] = alankodu + numara
        item['ilce'] = response.xpath('//*[@id="location"]/a[4]/a/span/text()')[0].extract()

        yield item


