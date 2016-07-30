import Prof_parse.items as items
from scrapy.contrib.loader.processor import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
from scrapy import selector
from scrapy.spiders import *
import scrapy.linkextractor
from scrapy.linkextractor import *


# class ProfLoader(ItemLoader):
#    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
#    default_output_processor = TakeFirst()


class ProfSpider(CrawlSpider):
    name = 'Prof'
    allowed_domains = ['apmath.spbu.ru']
    start_urls = ['http://www.apmath.spbu.ru/ru/staff/']
    rules = (
        Rule(scrapy.linkextractor.LinkExtractor(restrict_xpaths="//*[@id='content']/table/tr/td[1]/a"),
             callback='parse_prep_info'),
        # Rule(scrapy.linkextractor.LinkExtractor(allow='index.html'), callback='parse_prep_info')
    )

    def parse_prep_info(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        item = items.Prof()
        item['name'] = response.xpath("//*[@id='content']/h1/text()").extract()
        # item['desc'] = response.xpath("").extract()
        return item
        # name = response.xpath("//*[@id='content']/h1").extract()
        # self.logger.info(name)
        # self.logger.debug("12345")
