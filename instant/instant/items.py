# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy 
from scrapy.loader.processors import Join, MapCompose, TakeFirst
from six import ensure_text 
from w3lib.html import remove_tags
import datetime
import re

def set_string(string):
    string = string.replace("\n", "")
    return (string)

def format_string(string):

    tab = string.split(" ")
    day = ""
    month = ""
    year = ""
    for string in tab:
        if (re.match(r"\d{2}", string) and len(string) <= 2):
            day = string
            if (len(day) == 1):
                day = "0"+day
        elif (re.match(r"[a-zA-Z]", string)):
            long_month_name = string
            datetime_object = datetime.datetime.strptime(long_month_name, "%B")
            month = str(datetime_object.month)
            if (len(month) == 1):
                month = "0"+month
        elif (re.match(r"\d{4}", string)and len(string) == 4):
            year = string
    return(year + ":" + month + ":" + day)



def number(string):
    tab = re.findall(r"\D*(\d+)\D*", string)
    if (len(tab) != 0):
        return tab[0]
    else:
        return ""

def price_number(string):
    tab = re.findall(r"\D*(\d*\.?\d*)\D*", string)
    if (len(tab) != 0):
        return tab[0]
    else:
        return ""

class InstantItem(scrapy.Item):
    Title = scrapy.Field(
        input_processor = MapCompose(remove_tags, set_string), 
        output_processor = TakeFirst()
    )
    Plateform = scrapy.Field(
        input_processor = MapCompose(remove_tags, set_string), 
        output_processor =  MapCompose()
    )
    Release = scrapy.Field(
        input_processor = MapCompose(remove_tags, set_string, format_string), 
        output_processor =  TakeFirst() 
    )
    Tags = scrapy.Field(
        input_processor = MapCompose(remove_tags, set_string), 
        output_processor = MapCompose()
    )
    Flat_price = scrapy.Field(
        input_processor = MapCompose(remove_tags, price_number, set_string), 
        output_processor = TakeFirst() 
    )

    Discount = scrapy.Field(
        input_processor = MapCompose(remove_tags, number, set_string), 
        output_processor = TakeFirst()
        )

    Price = scrapy.Field(
        input_processor = MapCompose(remove_tags, price_number, set_string), 
        output_processor =  TakeFirst()
    )
    Developer = scrapy.Field(
        input_processor = MapCompose(remove_tags, set_string), 
        output_processor = MapCompose()
    )
    Publisher = scrapy.Field(
        input_processor = MapCompose(remove_tags, set_string), 
        output_processor = MapCompose()
    )
