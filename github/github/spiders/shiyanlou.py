# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou'
    allowed_domains = ['']
 #   start_urls = ['https://github.com/shiyanlou?page=1&tab=repositories']
    
    @property 
    def start_urls(self):
    	url_temp = 'https://github.com/shiyanlou?page={}&tab=repositories'
      	return(url_temp.format(i) for i in range(1,5))

    def parse(self, response):
    	for github in response.css('div#user-repositories-list li'):
    		item = GithubItem({
    			'name':github.css('h3 a::text').extract_first().strip(),
    			'update_time':github.css('relative-time::attr(datetime)').extract_first(),
    		})
    		yield item

        
