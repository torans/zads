# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZadsSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    pub_date = scrapy.Field()
    types = scrapy.Field()
    tags = scrapy.Field()
    view_count = scrapy.Field()
    content = scrapy.Field()