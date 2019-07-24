# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyPcItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位
    position = scrapy.Field()
    # 人数
    num = scrapy.Field()
    # 要求
    position_require = scrapy.Field()
