import scrapy
from ..items import ScrapAmazonItem
from scrapy.http import FormRequest


class QuoteSpider(scrapy.Spider):
    name = "quotes"  # name of the spider
    start_urls = ["https://quotes.toscrape.com/login"]
    page_number = 2

    def parse(self, response: object, **kwargs: object) -> object:
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(response=response,formdata= {
            "csrf_token":token,
            "username" : "myusername@example.com", 
            "password" : "myrandompassword"
        },callback=self.start_scraping)