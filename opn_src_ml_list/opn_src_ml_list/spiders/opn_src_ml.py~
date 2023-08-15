import scrapy
from ..items import OpnSrcMlListItem
from scrapy.linkextractors import LinkExtractor


class OpnSrcMLSpider(scrapy.Spider):
    # we don't need self here because these variables are class properties and not instance properties.
    name = "OpnSrcML"
    page_number = 2
    start_urls = ["https://github.com/collections/machine-learning?page=1"]


    def parse(self, response, **kwargs):
        link_extractor = LinkExtractor(restrict_css=("article div h1 a"))
        prj_urls = link_extractor.extract_links(response)
        item = OpnSrcMlListItem()
        all_article = response.css("article.my-5")
        prj_nms = all_article.xpath("//div/h1/a/@href").extract()

        for prj_nm, prj_url in zip(prj_nms, prj_urls):
            name = prj_nm.replace("/", " ").strip()
            url = prj_url.url
            if name[:4] not in url:
                continue
            item["prj_name"] = name
            item["url"] = url

            yield item

        next_page =f"https://github.com/collections/machine-learning?page={OpnSrcMLSpider.page_number}"
        if OpnSrcMLSpider.page_number < 3:
            OpnSrcMLSpider.page_number +=1
            yield scrapy.Request(url=next_page, callback=self.parse)

