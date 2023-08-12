import scrapy
from ..items import OpnSrcMlListItem
from scrapy.linkextractors import LinkExtractor

class OpnSrcMLSpider(scrapy.Spider):
    name = "OpnSrcML"
    start_urls = ["https://github.com/collections/machine-learning"]

    def parse(self, response, **kwargs):
        link_extractor = LinkExtractor(restrict_css=("article div h1 a"))
        prj_urls = link_extractor.extract_links(response)
        item = OpnSrcMlListItem()
        all_article = response.css("article.my-5")
        prj_nms = all_article.xpath("//div/h1/a/@href").extract()

        for prj_nm,prj_url in zip(prj_nms,prj_urls):
            item["prj_name"] = prj_nm
            item["url"] = prj_url.url
            yield item