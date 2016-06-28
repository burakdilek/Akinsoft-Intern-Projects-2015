# -*- coding: utf-8 -*-
__author__ = 'Hamdi Burak Dilek'
import scrapy
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from .. import items
from scrapy import log, Request

class tripadvisorSpider(CrawlSpider):
    name = "BsOtel"
    DOWNLOAD_DELAY = 1
    allowed_domains = ["tripadvisor.com.tr"]
    start_urls = [
        ## Bursa Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297977-Bursa-Hotels.html',
        'http://www.tripadvisor.com.tr/Hotels-g297977-oa30-Bursa-Hotels.html',
        ## Diyarbakır Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297993-Diyarbakir_Province-Hotels.html',
        ## Erzurum Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297995-c2-Erzurum_Province-Hotels.html',
        ## Eskişehir Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g319805-Eskisehir_Province-Hotels.html',
        ## Gaziantep Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g6739913-Gaziantep_Province-Hotels.html',
        'http://www.tripadvisor.com.tr/Hotels-g6739913-oa30-Gaziantep_Province-Hotels.html',
        ## Kayseri Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297984-Kayseri_Kayseri_Province-Hotels.html',
        ## Kocaeli Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g788070-Kocaeli_Province-Hotels.html',
        ## Konya Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g298013-Konya_Province-Hotels.html',
        'http://www.tripadvisor.com.tr/Hotels-g298013-oa30-Konya_Province-Hotels.html',
        ##'Şanlıurfa Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g494962-Sanliurfa_Province-Hotels.html',
        ##Kahramanmaraş Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1026579-Kahramanmaras_Province-Hotels.html',
        ##Van Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g298040-Van_Province-Hotels.html',
        ##Tekirdağ Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g780955-Tekirdag_Province-Hotels.html',
        ##Mardin Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g672770-Mardin_Province-Hotels.html',
        ##Malatya Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g298017-Malatya_Province-Hotels.html',
        ##Edirne Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g652368-Edirne_Province-Hotels.html',
        ## Kırklareli Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1202846-Kirklareli_Province-Hotels.html',
        ## Yalova Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g298042-Yalova_Province-Hotels.html',
        ##Sakarya Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g612462-Sakarya_Province-Hotels.html',
        ##Çanakkale Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297979-Canakkale_Canakkale_Province_Turkish_Aegean_Coast-Hotels.html',
        ##'Bilecik Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g2186706-Bilecik_Province-Hotels.html',
        ## Çankırı Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1156322-Cankiri_Province-Hotels.html',
        ## KIrşehir Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297985-Kirsehir_Kirsehir_Province-Hotels.html',
        ##Yozgat Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1211968-Yozgat_Province-Hotels.html',
        ##Sivas Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g298036-Sivas_Province-Hotels.html',
        ## NEvşehir Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297986-Nevsehir_Nevsehir_Province-Hotels.html',
        ## Aksaray Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g3218926-Aksaray_Province-Hotels.html',
        ## Niğde Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1597012-Nigde_Province-Hotels.html',
        ## Karaman Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1999788-Karaman_Province-Hotels.html',
        ## Bingöl Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g3445173-Bingol_Bingol_Province-Hotels.html',
        ## Ağrı Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g788020-Agri_Province-Hotels.html',
        ## Iğdır Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g672768-Igdir_Province-Hotels.html',
        ## Muş Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1075079-Mus_Province-Hotels.html',
        ## Bitlis Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g672765-Bitlis_Province-Hotels.html',
        ## Erzincan Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g780949-Erzincan_Province-Hotels.html',
        ## Elazığ Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g672769-Elazig_Province-Hotels.html',
        ## Ardahan Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g616256-Ardahan_Province-Hotels.html',
        ## Kars Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g298010-Kars_Province-Hotels.html',
        ## Tunceli Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g788039-Tunceli_Province-Hotels.html',
        ## Adıyaman Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g297956-Adiyaman_Province-Hotels.html',
        ## Siirt Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g780972-Siirt_Province-Hotels.html',
        ## Kilis Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g1075076-Kilis_Province-Hotels.html',
        ## Şırnak Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g780970-Sirnak_Province-Hotels.html',
        ##Batman Otelleri
        'http://www.tripadvisor.com.tr/Hotels-g672766-Batman_Province-Hotels.html'

    ]
    def my_range(start, end, step):
        while start <= end:
            yield start
            start += step

    rules = [Rule(LinkExtractor(allow=['/Hotel_Review.*']), 'parse_page')]
    def parse_page(self, response):

        item = items.BsotelscrapItem()
        item['isim'] = response.xpath('//*[@id="HEADING"]/text()')[1].extract()
        item['adres'] = response.xpath('//*[@id="HEADING_GROUP"]/div/div[3]/address/div[1]/span/span[1]/text()')[0].extract()
        item['sehir'] = response.xpath('//*[@id="BREADCRUMBS"]/li[4]/a/span/text()')[0].extract()

        yield item