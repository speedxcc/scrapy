# -*- coding: utf-8 -*-
import scrapy
from github.items import GithubItem

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou'
    allowed_domains = ['github.com']
 #   start_urls = ['https://github.com/shiyanlou?page=1&tab=repositories']
    
    @property 
    def start_urls(self):
    	url_temp = 'https://github.com/shiyanlou?page={}&tab=repositories'
      	return(url_temp.format(i) for i in range(1,5))

    def parse(self, response):
        for github in response.css('div#user-repositories-list li'):
#            item = GithubItem({
#                'name':github.css('h3 a::text').extract_first().strip(),
#                'update_time':github.css('relative-time::attr(datetime)').extract_first()
#                })
            item = GithubItem()
            item['name'] = github.css('h3 a::text').extract_first().strip()
            item['update_time'] = github.css('relative-time::attr(datetime)').extract_first()

            detail_url = response.urljoin(github.css('h3 a::attr(href)').extract_first())
            request = scrapy.Request(detail_url, callback=self.parse_detail)
            request.meta['item'] = item
            yield request

    def parse_detail(self, response):
        item = response.meta['item']
        item['commits'] = response.css('ul.numbers-summary span[class="num text-emphasized"]::text').extract()[0].strip()
        item['branches'] = response.css('ul.numbers-summary span[class="num text-emphasized"]::text').extract()[1].strip()
        item['releases'] = response.css('ul.numbers-summary span[class="num text-emphasized"]::text').extract()[2].strip()
        yield item





        
