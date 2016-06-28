# -*- coding: utf-8 -*-
__author__ = 'Hamdi Burak Dilek'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request
##http://www.bulurum.com/search/Di%C5%9F-Laboratuvarlar%C4%B1/
"http://www.bulurum.com/details/771d43cd5gab7__b3h344g7d3_554770?what=Di%C5%9F%20Laboratuvarlar%C4%B1&where="
class tripadvisorSpider(CrawlSpider):
    name = "disLabaratuari"
    DOWNLOAD_DELAY = 10
    allowed_domains = ["bulurum.com"]
    start_urls = [
        "http://www.bulurum.com/search/Di%C5%9F-Laboratuvarlar%C4%B1/"
    ]
    for i in range(1,9):
        start_urls.append("http://www.bulurum.com/search/Di%C5%9F-Laboratuvarlar%C4%B1?page="+str(i))
    rules = [Rule(LinkExtractor(allow=['/details/.*.Laboratuvarları&where=']), 'parse_page')]
    def parse_page(self, response):
        item = items.ScrapdataItem()
        item['isim'] = response.xpath('//*[@id="ctl00_ContentRoot_DetailsPage_rgnbreadcrumb"]/div/nav/span[6]/span/text()')[0].extract()
        item['adres'] = response.xpath('//*[@id="ctl00_ContentRoot_DetailsPage_RecordControl_AddressLbl"]/text()')[0].extract()
        item['sehir'] = response.xpath('//*[@id="ctl00_ContentRoot_DetailsPage_rgnbreadcrumb"]/div/nav/span[2]/a/span/text()')[0].extract()
        item['ilce'] = response.xpath('//*[@id="ctl00_ContentRoot_DetailsPage_rgnbreadcrumb"]/div/nav/span[3]/a/span/text()')[0].extract()
        ##telefon list index'i yanlış olabilir
        item['tel'] = response.xpath('//*[@id="ctl00_ContentRoot_DetailsPage_RecordControl_phones"]/meta/@content')[0].extract()

        yield item