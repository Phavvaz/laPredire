import scrapy
import numpy as np


class predireSpider(scrapy.Spider):
    name = 'Predire'

    def start_requests(self):
        urls = []
        for x in np.arange(2000, 2021):
            urls.append(
                f"https://www.skysports.com/barcelona-results/{x}-{x+1}")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for x in response.css('div.fixres__item'):
            r = {
                'Season': response.url.split('/')[-1],
                'Home': x.css('.swap-text__target::text')[0].get(),
                'Away': x.css('.swap-text__target::text')[1].get(),
                'Home_score': x.css('.matches__teamscores-side::text')[0].get(),
                'Away_score': x.css('.matches__teamscores-side::text')[1].get()
            }
            yield r


class predireSpider2(scrapy.Spider):
    name = 'Predire_fixtDates'

    def start_requests(self):
        urls = []
        for x in np.arange(2000, 2021):
            urls.append(
                f"https://www.skysports.com/barcelona-results/{x}-{x+1}")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for z in response.css('h4'):
            q = {
                'Date': z.css('.fixres__header2::text').get(),
            }
            yield q


class predireSpider3(scrapy.Spider):
    name = 'Predire_fixtComp'

    def start_requests(self):
        urls = []
        for x in np.arange(2000, 2021):
            urls.append(
                f"https://www.skysports.com/barcelona-results/{x}-{x+1}")
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for z in response.css('h5'):
            c = {
                'Competition': z.css('.fixres__header3::text').get(),
            }

            yield c


class predireTestSpider(scrapy.Spider):
    name = 'PredireTest'

    def start_requests(self):
        url = "https://www.skysports.com/barcelona-fixtures/2021-22"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for x in response.css('div.fixres__item'):
            r = {
                'Season': response.url.split('/')[-1],
                'Home': x.css('.swap-text__target::text')[0].get(),
                'Away': x.css('.swap-text__target::text')[1].get()
            }
            yield r
