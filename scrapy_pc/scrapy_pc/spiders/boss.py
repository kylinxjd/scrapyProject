# -*- coding: utf-8 -*-
import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['www.zhipin.com/c101210100/?query=python']
    start_urls = ['http://www.zhipin.com/c101210100/?query=python&page=1&ka=page-1']

    def parse(self, response):

        ret = response.xpath('//ul/li')

        for position_node in ret:

            position = position_node.xpath('./div[@class="job-primary"]/div/h3/a/div[@class="job-title"]/text()').extract()
            print(position)

        print(len(ret))
