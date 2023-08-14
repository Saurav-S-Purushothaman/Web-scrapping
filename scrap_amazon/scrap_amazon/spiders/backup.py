import scrapy
from ..items import ScrapAmazonItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"  # name of the spider
    start_urls = ["https://quotes.toscrape.com"]
    page_number = 2

    def parse(self, response: object, **kwargs: object) -> object:
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

    #    next_page =
    #    print(f"page : {next_page}")
    #    if next_page is not None:
    #        yield response.follow(next_page,callback=self.parse)
