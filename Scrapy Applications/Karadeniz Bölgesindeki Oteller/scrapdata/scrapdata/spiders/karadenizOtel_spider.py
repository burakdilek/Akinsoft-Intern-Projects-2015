# -*- coding: utf-8 -*-
__author__ = 'Hamdi Burak Dilek'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class tripadvisorSpider(CrawlSpider):
    name = "karadenizOtel"
    DOWNLOAD_DELAY = 1
    allowed_domains = ["tripadvisor.com.tr"]
    start_urls = [
    ]
    def my_range(start, end, step):
        while start <= end:
            yield start
            start += step

    for i in my_range(0, 180, 30):
        start_urls.append('http://www.tripadvisor.com.tr/Hotels-g673665-oa'+str(i)+'-Turkish_Black_Sea_Coast-Hotels.html')
    rules = [Rule(LinkExtractor(allow=['/Hotel_Review.*'],), 'parse_page')]
    def parse_page(self, response):

        item = items.KaradenizotelscrapItem()
        item['isim'] = response.xpath('//*[@id="HEADING"]/text()')[1].extract()
        item['adres'] = response.xpath('//*[@id="HEADING_GROUP"]/div/div[3]/address/div[1]/span/span[1]/text()')[0].extract()
        item['sehir'] = response.xpath('//*[@id="BREADCRUMBS"]/li[4]/a/span/text()')[0].extract()
        item['ilce'] = response.xpath('//*[@id="BREADCRUMBS"]/li[5]/a/span/text()')[0].extract()

        yield item