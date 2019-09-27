# -*- coding: utf-8 -*-
import scrapy
import fake_useragent
from scrapy.selector import Selector
from maoyan.items import MaoyanItem

headers = {
    'user-agent': fake_useragent.UserAgent(verify_ssl=False).chrome
}


class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['www.maoyan.com/board/4']
    start_urls = ['https://www.maoyan.com/board/4?offset=%s']

    def start_requests(self):
        for i in range(10):
            url = self.start_urls[0] % (i*10)
            yield scrapy.Request(url, callback=self.parse, dont_filter=False, headers=headers)

    def parse(self, response):
        sel = Selector(response)
        item = MaoyanItem()
        for movie in sel.xpath('//dl["board-wrapper"]/dd'):
            item['title'] = movie.xpath('a/@title').extract_first()
            item['link'] = 'https://www.maoyan.com' + movie.xpath('a/@href').extract_first()
            yield item
