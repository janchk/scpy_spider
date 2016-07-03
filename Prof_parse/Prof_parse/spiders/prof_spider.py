import scrapy, items
from scrapy.contrib.loader.processor import TakeFirst, MapCompose
from scrapy.loader import ItemLoader
from scrapy import selector
from scrapy.spiders import *
import scrapy.linkextractor
from scrapy.linkextractor import *


class ProfLoader(ItemLoader):
    default_input_processor = MapCompose(lambda s: re.sub('\s+', ' ', s.strip()))
    default_output_processor = TakeFirst()


class ProfSpider(CrawlSpider):
    name = 'Prof'
    allowed_domains = ['apmath.spbu.ru']
    start_urls = ['http://www.apmath.spbu.ru/ru/staff/']
    rules = (
        Rule(scrapy.linkextractor.LinkExtractor(restrict_xpaths='//tbody/tr'), follow=True),
        Rule(scrapy.linkextractor.LinkExtractor(allow='index.html'), callback='parse_prep_info')
    )

    def parse_prep_info(self, response):
        xhs = selector.HtmlXPathSelector(response)

        l = ProfLoader(items.ProfItem, xhs)
        l.add_xpath()

        return l.load_item()






