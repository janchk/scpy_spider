import scrapy


class ProfItem(scrapy.Item):
    name = scrapy.Field()
    photo = scrapy.Field()
    interests = scrapy.Field()
    #add more later
