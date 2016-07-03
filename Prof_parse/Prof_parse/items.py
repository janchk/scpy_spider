# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProfParseItem(scrapy.Item):
    name = scrapy.Field()
    photo = scrapy.Field()
    interests = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

#  class ProfItem(scrapy.Item):
#      name = scrapy.Field()
#      photo = scrapy.Field()
#      interests = scrapy.Field()
#      #add more later
#