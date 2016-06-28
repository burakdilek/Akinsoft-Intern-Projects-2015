# -*- coding: utf-8 -*-
__author__ = 'AS'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class tripadvisorSpider(CrawlSpider):
    name = "istanbulrestorant"
    DOWNLOAD_DELAY = 1
    allowed_domains = ["tripadvisor.com.tr"]
    start_urls = [
    ]
    def my_range(start, end, step):
        while start <= end:
            yield start
            start += step

    for i in my_range(30, 10950, 30):
        start_urls.append('http://www.tripadvisor.com.tr/Restaurants-g293974-oa'+str(i)+'-Istanbul.html')
    rules = [Rule(LinkExtractor(allow=['/Restaurant_Review.*']), 'parse_page')]
    def parse_page(self, response):

        item = items.IstanbulrestorantscrapItem()
        item['isim'] = response.xpath('//*[@id="BREADCRUMBS"]/li[last()]/text()')[0].extract()
        item['adres'] = response.xpath('//*[@id="ABOVE_THE_FOLD"]/div[1]/div[2]/div/div[2]/div/div[1]/div/address/span/span/span[1]/text()')[0].extract()
        item['tel'] = response.xpath('//*[@id="ABOVE_THE_FOLD"]/div[1]/div[2]/div/div[2]/div/div[1]/div/div/div/div[1]/div/text()')[0].extract()


        yield item


