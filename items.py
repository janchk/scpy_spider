import scrapy


class ProfItem(scrapy.Item):
    name = scrapy.Field()