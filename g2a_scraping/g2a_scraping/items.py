# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import itemloaders
from itemloaders.processors import MapCompose, TakeFirst
import scrapy


class G2AScrapingItem(scrapy.Item):
    # define the fields for your item here like:
    def remove_whitespace(value):
        return value.strip()

    Title = scrapy.Field()
    Plateform = scrapy.Field()
    Release = scrapy.Field()
    Flat_price = scrapy.Field()
    Discount = scrapy.Field()
    Price = scrapy.Field()
    
