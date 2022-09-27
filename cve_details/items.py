# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


import scrapy

class CveItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    cveid = scrapy.Field()
    score = scrapy.Field()
    vulntype = scrapy.Field()
    vendor = scrapy.Field()
    product = scrapy.Field()
    producttype = scrapy.Field()
    version = scrapy.Field()
