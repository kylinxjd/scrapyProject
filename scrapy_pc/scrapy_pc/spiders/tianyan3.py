# -*- coding: utf-8 -*-
import re

import scrapy

from scrapy_pc.items import ScrapyPcItem


class Tianyan3Spider(scrapy.Spider):
    name = 'tianyan3'
    allowed_domains = ['www.skeyedu.com']
    start_urls = ['http://www.skeyedu.com/']

    def parse(self, response):

        url = response.xpath('//div[@id="header"]/ul/li[6]/a/@href').extract()[0]

        url = self.start_urls[0] + url

        yield scrapy.Request(url=url, callback=self.second_url_handler)

    def second_url_handler(self, response):

        position_nodes = response.xpath('//div[@class="zhiwei"]')

        items = []

        for node in position_nodes:

            position = node.xpath('./span[@class="zhaopin_zw"]/text()').extract()[0]
            num = node.xpath('./span[@class="zhaopin_rs"]/text()').extract()[0]
            position_require_list = node.xpath('./p[@class="zhaopin_yq"]/text()').extract()

            position_require = ''.join(position_require_list)

            position_require = re.sub(r'[\s]', '', position_require)

            item = ScrapyPcItem()

            item['position'] = position
            item['num'] = num
            item['position_require'] = position_require

            items.append(item)

        print(items)

        return items