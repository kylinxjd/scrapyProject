# -*- coding: utf-8 -*-
import scrapy

from scrapy_pc.items import ScrapyPcItem


class TianyanSpider(scrapy.Spider):
    name = 'tianyan'
    allowed_domains = ['skeyedu.com']
    start_urls = ['http://www.skeyedu.com/']

    def parse(self, response):
        recruit_url = response.selector.xpath('//*[@id="header"]/ul/li[6]/a/@href')[0].extract()

        recruit_detail_url = self.start_urls[0] + recruit_url

        # print("Ssssssssssssssssssssssssssssss")
        # print(recruit_detail_url)

        yield scrapy.Request(url=recruit_detail_url, callback=self.second_handler)

    def second_handler(self, response):
        node_list = response.xpath('//div[@class="zhiwei"]')
        items = []

        for node in node_list:
            position = node.xpath('./span[@class="zhaopin_zw"]/text()')[0].extract()
            num = node.xpath('./span[@class="zhaopin_rs"]/text()')[0].extract()
            position_require_infolist = node.xpath('./p[@class="zhaopin_yq"]/text()').extract()
            position_require = ''.join(position_require_infolist)
            position_require.strip()
            position_require = position_require.replace(' ', '').replace('\t', '').replace('\r\n', '')

            # print("aaaaaaaaaaaaaaaaaaaaaa")
            # print(position)
            # print(num)
            print(position_require)

            item = ScrapyPcItem()

            item['position'] = position
            item['num'] = num
            item['position_require'] = position_require

            items.append(item)

        #   抛出
        return items
