# run with "scrapy runspider -o wineries.csv wineries.py"

#https://www.wine-searcher.com/biz/producers/usa

import scrapy
from scrapy.crawler import CrawlerProcess
import requests 

import googlemaps
from datetime import datetime

from random import randint
from time import time, sleep

#USER_AGENT = 'MyCompany-MyCrawler (bot@mycompany.com)'
#ROBOTSTXT_OBEY = True
#DOWNLOAD_DELAY = 5.0
#UTOTHROTTLE_ENABLED = True
#TTPCACHE_ENABLED = True

start_time = time()
#req =0

class VAwineSpider(scrapy.Spider):
    name = 'vawinespider'
    allowed_domains = ['wine-searcher.org']
    #download_delay = 0.5
    start_urls = ['https://www.wine-searcher.com/biz/producers/usa']

    def parse(self, response):
        for result in response.css('table'):
            name = result.css('td >a::text').extract_first()
            #lon = result.css('div::attr(data-longitude)').extract_first()
            #lat = result.css('div::attr(data-latitude)').extract_first()
            #elev = requests.get('https://maps.googleapis.com/maps/api/elevation/json?location=lat,lon').text
            #region = result.css('.region-list-link::text').extract_first()
            #address = result.css('address.result-text::text')[0].extract()
            #address1 = result.css('address.result-text::text')[1].extract()
            
            yield {
                'name': name
                #'region': region,
                #'address': address,
                #'town': address1,
                #'lat': lon,
                #'lon': lat
            }
            #next = response.css('.pagination > a[rel="next"]::attr(href)').extract_first()

            elapsed_time = time() - start_time
            dt = float(randint(10,100)/200)
            sleep(dt) # wait 0.5 second on average
            #req += 1
            #if next:
            #    yield response.follow(next, self.parse)

