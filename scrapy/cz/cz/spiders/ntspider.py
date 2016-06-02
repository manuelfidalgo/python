###########################################CZ
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from cz.items      import CZItem

class MySpider(CrawlSpider):
    name = 'mycr'  
    price_exp = "//span[starts-with(@id,'product-price')]//span//text()"
    description_exp = "id('product_addtocart_form')//div[3]//div[1]//h1"
    baseURL = ""
    name        = "cz"
    allowed_domains = [baseURL]
    start_urls  = ["http://"+baseURL]

    rules = (
        Rule(LinkExtractor(allow=r'/*',allow_domains=baseURL), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        prices  = response.xpath(MySpider.price_exp).extract()
        descriptions = response.xpath(MySpider.description_exp).extract()
        if prices and descriptions: 
            item = CZItem()
            item['url'] = response.url
            item['price'] = prices[0]
            item['title'] = descriptions[0]
            return item
