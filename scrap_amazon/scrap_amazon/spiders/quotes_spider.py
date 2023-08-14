import scrapy
from ..items import ScrapAmazonItem
from scrapy.utils.response import open_in_browser
from scrapy.http import FormRequest


class QuoteSpider(scrapy.Spider):
    name = "quotes"  # name of the spider
    start_urls = ["https://quotes.toscrape.com/login"]
    page_number = 2

    def parse(self, response: object, **kwargs: object) -> object:
        token = response.css("form input::attr(value)").extract_first()
        return FormRequest.from_response(
            response=response,
            formdata={
                "csrf_token": token,
                "username": "myusername@example.com",
                "password": "myrandompassword",
            },
            callback=self.start_scraping,
        )

    def start_scraping(self, response):
        open_in_browser(response)
        items = ScrapAmazonItem()
        all_div_tags = response.css("div.quote")
        for quote in all_div_tags:
            title = quote.css("span.text::text").extract()
            author = quote.css("span small.author::text").extract()
            tag = quote.css(".tag::text").extract()
            items["title"] = " ".join(title)
            items["author"] = " ".join(author)
            items["tag"] = " ".join(tag)
            yield items

        page_number = 2

        next_page = "https://quotes.toscrape.com/page/" + str(page_number) + "/"
        print(f"\n\n{page_number}\n\n")
        if QuoteSpider.page_number < 11:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
