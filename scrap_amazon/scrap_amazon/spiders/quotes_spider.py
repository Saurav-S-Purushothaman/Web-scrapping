import scrapy
from ..items import ScrapAmazonItem


class QuoteSpider(scrapy.Spider):
    name = "quotes"  # name of the spider
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response: object, **kwargs: object) -> object:
        """Function to parse url, crawl using xpath/css
            selector

        Args:
            response (scrapy.http.response.html.HtmlResponse): Response from url

        Yields:
            ScrapAmazonItem.item : output or result
        """
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

