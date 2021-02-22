# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.spiders import CrawlSpider, Rule
from scrapy.http import Request
from scrapy.linkextractors import LinkExtractor
from scrapy import Selector
from selenium import webdriver
import random
import time

# This is a combined code of Scrapy and Selenium.All the fields are fetched using scrapy but we faced issue of getting 
#"Lazyimage" for the picture of the player_of_match. To meet that , selenium code is appended.
class EspnmatchDetailsSpider(Spider):

    # specific domain allowed to be crawled with the url name 
    name = 'group7_matchDetails'
    allowed_domains = ['espncricinfo.com']
    start_urls = ['https://www.espncricinfo.com/series/icc-cricket-world-cup-2019-1144415/match-results/']
    
    

    # the callback function whenever the main URL is crawled successfully
    def parse(self, response):              
       
                
        matches=response.xpath('//a[contains(@class,"match-info-link-FIXTURES")]/@href').extract()        
        for match in matches:
            absolute_match_url = response.urljoin(match)          
            yield Request(absolute_match_url,callback=self.parse_match)
            
            
    # the callback function whenever the respective match-results URL is crawled successfully                
    def parse_match(self, response):
        
        match_url=response.url
        
        # Selenium test scripts in google chrome.
        driver = webdriver.Chrome(executable_path='C:/Users/mohua/Downloads/chromedriver.exe')          
        driver.get(match_url)
        
        #Selenium Webdriver waits for the specified time, irrespective of the element is found or not, to increase the execution time of the script.
        time.sleep(random.choice([0, 2, 4, 6, 8, 14,23]))
        photo_player = driver.find_elements_by_xpath("//div[contains(@class, 'best-player-content')]/img")
        photo_player_list = [img_src.get_attribute("src") for img_src in photo_player]
        
        # this helps to fetch the match_referee field from the table
        rows = response.xpath('//*[@class="w-100 table match-details-table"]//tbody//tr//td//h5//text()').extract()
        
        
        # Scraping the required 8 fields about each match played in "icc cricket world cup 2019"
        scraped_info = {
                'URL':response.url,
                'PLAYER_NAME': response.css('.best-player-name a::text').get(default='').strip(),
                'Player of the match with the picture':photo_player_list,
                'Country that the player of the match belongs to':response.css('.best-player-team-name::text').get(default='').strip(),
                'Runs scored by every batsman':response.css('.batsman tbody td.font-weight-bold::text').extract(),
                'Balls played by every batsman': response.css('.batsman .font-weight-bold+ td::text').extract(),
                'Strike rate for every batsman': response.css('.batsman td:nth-child(8)::text').extract(),
                'Wickets taken by every bowler': response.css('.bowler td:nth-child(5)::text').extract(),
                'Economy rate for every bowler':response.css('.bowler td:nth-child(6)::text').extract(),
                'which country won the toss': response.css('tr:nth-child(2) .border-right+ td::text').extract(),
                'who were the umpires?': response.css('.multiple-detail-table-values').css('.player-details').css('.label::text').extract(),
                'who was the match referee':rows[len(rows)-1],
                }
        yield scraped_info       
        
            
    
    

        