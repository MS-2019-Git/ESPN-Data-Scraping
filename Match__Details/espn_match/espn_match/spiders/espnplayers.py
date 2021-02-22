# -*- coding: utf-8 -*-
import scrapy


class EspnplayersSpider(scrapy.Spider):
    name = 'espnplayers'
    allowed_domains = ['https://www.espncricinfo.com/series/icc-cricket-world-cup-2019-1144415/india-vs-new-zealand-1st-semi-final-1144528/full-scorecard']
    start_urls = ['http://https://www.espncricinfo.com/series/icc-cricket-world-cup-2019-1144415/india-vs-new-zealand-1st-semi-final-1144528/full-scorecard/']

    def parse(self, response):
        pass
