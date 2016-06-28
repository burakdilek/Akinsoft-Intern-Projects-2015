# -*- coding: utf-8 -*-
from scrapy.core.downloader.handlers.http11 import _ResponseReader

__author__ = 'Hamdi Burak Dilek'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class tripadvisorSpider(CrawlSpider):
    name = "franchiseFirma"
    DOWNLOAD_DELAY = 1
    allowed_domains = ["iskuruyorum.com"]
    start_urls = [
        'http://www.iskuruyorum.com/bayilikler/taki-aksesuar-bayilik-veren-firmalar/26/',
        'http://www.iskuruyorum.com/bayilikler/arac-bakim-onarim-hizmetleri-bayilik-veren-firmalar/3/',
        'http://www.iskuruyorum.com/bayilikler/oyuncak-hediyelik-bayilik-veren-firmalar/39/',
        'http://www.iskuruyorum.com/bayilikler/hirdavat-bayilik-veren-firmalar/14/',
        'http://www.iskuruyorum.com/bayilikler/kirtasiye-bayilik-veren-firmalar/31/',
        'http://www.iskuruyorum.com/bayilikler/mutfak-bayilik-veren-firmalar/35/',
        'http://www.iskuruyorum.com/bayilikler/zuccaciye-bayilik-veren-firmalar/41/',
        'http://www.iskuruyorum.com/bayilikler/otomat-bayilik-veren-firmalar/36/',
        'http://www.iskuruyorum.com/bayilikler/mucevherat-bayilik-veren-firmalar/28/',
        'http://www.iskuruyorum.com/bayilikler/emlak-bayilik-veren-firmalar/12/',
        'http://www.iskuruyorum.com/bayilikler/rent-a-car-arac-kiralama-bayilik-veren-firmalar/44/',
        'http://www.iskuruyorum.com/bayilikler/kargo-kurye-bayilik-veren-firmalar/43/'

    ]

    for i in range(1,11):
        start_urls.append('http://www.iskuruyorum.com/bayilikler/gida-bayilik-veren-firmalar/13/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/cafetatlipasta-bayilik-veren-firmalar/5/'+str(i)+'/')
    for i in range(1,5):
        start_urls.append('http://www.iskuruyorum.com/bayilikler/yapi-malzemesi-bayilik-veren-firmalar/40/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/fast-food-bayilik-veren-firmalar/10/'+str(i)+'/')

    for i in range(1,6):
        start_urls.append('http://www.iskuruyorum.com/bayilikler/bilgisayar-elektronik-bayilik-veren-firmalar/52/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/egitim-dersane-bayilik-veren-firmalar/9/'+str(i)+'/')

    for i in range(1,7):
        start_urls.append('http://www.iskuruyorum.com/bayilikler/diger-bayilik-veren-firmalar/51/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/mobilya-ev-tekstili-dekorasyon-bayilik-veren-firmalar/8/'+str(i)+'/')

    for i in range(1,2):
        start_urls.append('http://www.iskuruyorum.com/bayilikler/kuru-islak-temizleme-bayilik-veren-firmalar/42/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/saglik-bayilik-veren-firmalar/45/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/giyim-bayilik-veren-firmalar/50/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/otomotiv-yedek-parca-bayilik-veren-firmalar/38/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilik/toplu-sms-plus-bayilik/12358/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/isitma-sogutma-bayilik-veren-firmalar/30/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/ayakkabi-canta-bayilik-veren-firmalar/1/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/icecek-bayilik-veren-firmalar/15/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/restorant-bayilik-veren-firmalar/29/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/kozmetik-bayilik-veren-firmalar/33/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/bebek-cocuk-urunleri-bayilik-veren-firmalar/4/'+str(i)+'/')


    for i in range(1,4):
        start_urls.append('http://www.iskuruyorum.com/bayilikler/insaat-proje-tesisat-bayilik-veren-firmalar/49/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/oto-bakim-bayilik-veren-firmalar/37/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/enerji-bayilik-veren-firmalar/32/'+str(i)+'/')

    for i in range(1,3):
        start_urls.append('http://www.iskuruyorum.com/bayilikler/temizlik-guvenlik-bayilik-veren-firmalar/47/'+str(i)+'/')
        start_urls.append('http://www.iskuruyorum.com/bayilikler/cigkofte-bayilik-veren-firmalar/56/'+str(i)+'/')


    rules = [Rule(LinkExtractor(allow=['/bayilik/.*'],), 'parse_page')]



    def parse_page(self, response):

        item = items.FranchisefirmascrapItem()
        item['isim'] = response.xpath('//title/text()')[0].extract()
        item['adres'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[8]/div[position()=last()-1]/div[2]/ul/li[2]/text()')[0].extract()
        item['tel'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[8]/div[position()=last()-1]/div[2]/ul/li[3]/text()')[0].extract()
        item['yetkili'] = response.xpath('/html/body/div[4]/div/div[2]/div/div[8]/div[position()=last()-1]/div[2]/ul/li[1]/text()')[0].extract()
        yield item