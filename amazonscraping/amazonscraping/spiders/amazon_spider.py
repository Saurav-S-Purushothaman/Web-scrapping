import scrapy
from ..items import AmazonscrapingItem


class AmazonSpiderSpider(scrapy.Spider):
    name = "amazon_spider"
    start_urls = ["https://www.amazon.in/s?k=game+of+thrones+books&crid=16K6WXQK2KGEH&sprefix=game+of+thrones+book%2Caps%2C260&ref=nb_sb_noss_1"]

    def parse(self, response):
        item = AmazonscrapingItem()

        book_names = response.css(".a-color-base.a-text-normal").css("::text").extract()
        item["book_name"] = book_names
        yield item
        
