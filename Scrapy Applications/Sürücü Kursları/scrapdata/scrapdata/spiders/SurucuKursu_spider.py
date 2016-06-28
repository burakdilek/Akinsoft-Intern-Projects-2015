# -*- coding: utf-8 -*-
__author__ = 'Hamdi Burak Dilek'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class tripadvisorSpider(CrawlSpider):
    name = "surucuKursu"
    DOWNLOAD_DELAY = 1
    allowed_domains = ["ehliyetsinavsorularicoz.net"]
    start_urls = [
        "http://www.ehliyetsinavsorularicoz.net/index.php/turkiye-surucu-kurslari-listesi.html",
        "http://www.ehliyetsinavsorularicoz.net/index.php/turkiye-surucu-kurslari-listesi.html?start=25",
        "http://www.ehliyetsinavsorularicoz.net/index.php/turkiye-surucu-kurslari-listesi.html?start=50"
    ]
    rules = [Rule(LinkExtractor(allow=['/index.php/.*.surucu-kurslari.html']), 'parse_page')]
    def parse_page(self, response):
        item = items.ScrapdataItem()
        for sel in response.xpath('//*[@id="system"]/article/div/table/tbody'):
            a = sel.xpath('tr/td[4]/span/text()').extract()
            for i in range(len(a)):
                item['isim'] = sel.xpath('tr/td[4]/span/text()')[i].extract()
                item['adres'] = sel.xpath('tr/td[5]/span/text()')[i].extract()
                item['sehir'] = sel.xpath('tr/td[2]/span/text()')[i].extract()
                item['tel'] = sel.xpath('tr/td[6]/span/text()')[i].extract()
                item['ilce'] = sel.xpath('tr/td[3]/span/text()')[i].extract()

                yield item