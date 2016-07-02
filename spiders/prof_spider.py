import scrapy
from scrapy.spiders import *
from scrapy.linkextractor import *


class ProfSpider(CrawlSpider):
    name = 'Prof'
    allowed_domains = ['apmath.spbu.ru']
    start_urls = ['http://www.apmath.spbu.ru/ru/staff/']
    rules = (
        Rule(LinkExtractor(allow='/ru/staff/'), follow=True),
        Rule(LinkExtractor(allow='index.html'), callback='parse_item')
    )

