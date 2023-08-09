import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quotes"  # name of our spider
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
        """ Function to parse url, crawl using xpath/css 
            selector

        Args:
            response (scrapy.http.response.html.HtmlResponse): Response from url

        Yields:
            dictionary: output or result
        """
        all_div_tags = response.css("div.quote")
        for quote in all_div_tags:
            title = quote.css("span.text::text").extract()
            author = quote.css("span small.author::text").extract()
            tags = quote.css(".tag::text").extract()
            yield {
                "title":title,
                "author":author,
                "tags":tags
            }
