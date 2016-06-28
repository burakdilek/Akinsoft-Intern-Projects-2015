# -*- coding: utf-8 -*-
__author__ = 'Hamdi Burak Dilek'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request
##http://www.telerehber.com/index.asp?CID=1416&pg=13&uid=0
##http://www.telerehber.com/index.asp?CID=1416&pg=5&uid=0
##http://www.telerehber.com/firma_ayrinti.asp?fid=294480&uid=0&cid=1416
##http://www.telerehber.com/firma_ayrinti.asp?fid=535269&uid=0&cid=1416
class tripadvisorSpider(CrawlSpider):
    name = "otopark"
    DOWNLOAD_DELAY = 1
    allowed_domains = ["telerehber.com"]
    start_urls = [

    ]
    for i in range(1,44):
        start_urls.append("http://www.telerehber.com/index.asp?CID=1416&pg="+str(i)+"&uid=0")

    rules = [Rule(LinkExtractor(allow=['/firma_ayrinti.*.1416']), 'parse_page')]
    def parse_page(self, response):
        item = items.ScrapdataItem()
        item['isim'] = response.xpath('/html/body/center/center[2]/table[1]/tr[1]/td[2]/ul/font/b/text()')[0].extract()
        item['sehir'] = response.xpath('/html/body/center/center[2]/table[1]/tr[3]/td[2]/ul/table/tr[2]/td[2]/font/b/text()')[0].extract()
        item['adres'] = response.xpath('/html/body/center/center[2]/table[1]/tr[3]/td[2]/ul/table/tr[2]/td[2]/font/text()')[0].extract()

        yield item