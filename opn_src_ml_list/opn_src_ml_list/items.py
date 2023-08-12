# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class OpnSrcMlListItem(scrapy.Item):
    prj_name = scrapy.Field()
    url = scrapy.Field()