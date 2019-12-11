# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GameHotelItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Time = scrapy.Field()
    hotel_name = scrapy.Field()
    room_type = scrapy.Field()
    status = scrapy.Field()
    price = scrapy.Field()
    pass
