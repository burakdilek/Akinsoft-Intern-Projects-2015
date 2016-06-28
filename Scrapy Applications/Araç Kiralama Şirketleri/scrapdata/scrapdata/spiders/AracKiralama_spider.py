# -*- coding: utf-8 -*-
__author__ = 'Hamdi Burak Dilek'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request
##http://www.turkiyerentacar.net/25_firmalar.html
##http://www.turkiyerentacar.net/330-alize-rent-a-car.htm
class tripadvisorSpider(CrawlSpider):
    name = "aracKiralama"
    DOWNLOAD_DELAY = 2
    allowed_domains = ["turkiyerentacar.net"]
    start_urls = [

    ]
    for i in range(1,25):
        start_urls.append("http://www.turkiyerentacar.net/"+str(i)+"_firmalar.html")
    rules = [Rule(LinkExtractor(allow=['/\d+-.*.htm']), 'parse_page')]
    def parse_page(self, response):
        item = items.ScrapdataItem()
        item['isim'] = response.xpath('//*[@id="contentmiddle"]/div/ul/li[1]/h1/text()')[0].extract()
        item['tel'] = response.xpath('//*[@id="contentmiddle"]/div/ul/li[3]/text()')[0].extract()
        item['adres'] = response.xpath('//*[@id="contentmiddle"]/div/ul/li[6]/text()')[0].extract()


        yield item