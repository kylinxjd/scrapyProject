# -*- coding: utf-8 -*-
import scrapy

from scrapy_pc.items import ScrapyPcItem


class Tianyan2Spider(scrapy.Spider):
    name = 'tianyan2'
    allowed_domains = ['www.skeyedu.com']
    start_urls = ['http://www.skeyedu.com/']

    def parse(self, response):
        # 获取详情页url
        second_url = response.xpath('//*[@id="header"]/ul/li[6]/a/@href').extract()[0]

        url = self.start_urls[0] + second_url

        # 抓取二级路径的信息
        yield scrapy.Request(url=url, callback=self.second_handler, method='GET')

    def second_handler(self, response):
        # 获取招聘节点
        node_list = response.xpath('//div[@class="zhiwei"]')

        items = []

        for node in node_list:

            position = node.xpath('./span[@class="zhaopin_zw"]/text()').extract()[0]

            num = node.xpath('./span[@class="zhaopin_rs"]/text()').extract()[0]

            position_require_list = node.xpath('./p[@class="zhaopin_yq"]/text()').extract()

            position_require = ''.join(position_require_list).strip().replace(' ', '').replace('\t', '').replace('\r\n', '')

            item = ScrapyPcItem()

            item['position'] = position
            item['num'] = num
            item['position_require'] = position_require

            items.append(item)
        # 抛出
        return items























