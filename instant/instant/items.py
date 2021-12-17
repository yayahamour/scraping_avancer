# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy 
from scrapy.loader.processors import Join, MapCompose, TakeFirst 
from w3lib.html import remove_tags
import re

def set_date(string):
    pass
def number(string):
    return(re.findall(r".*([0-9]+).*", string)[0])

class InstantItem(scrapy.Item):
    Title = scrapy.Field()
    Plateform = scrapy.Field()
    Release = scrapy.Field()
    Tags = scrapy.Field()
    Flat_price = scrapy.Field()

    Discount = scrapy.Field()

    Price = scrapy.Field()
    Developer = scrapy.Field()
    Publisher = scrapy.Field()
