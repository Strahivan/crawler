# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class NovelshipCrawlerItem(scrapy.Item):
    title = Field()
    price = Field()
    customer_id = Field()
    location = Field()

    # to be implemented
    descriptions = Field()
    image = Field()
