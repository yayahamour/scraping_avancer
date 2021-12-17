from types import prepare_class
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from instant.items import InstantItem
from scrapy.loader import ItemLoader

class InstantGamingSpider(CrawlSpider):
    name = 'instant-gaming'
    allowed_domains = ['instant-gaming.com']
    start_urls = ['https://www.instant-gaming.com/en/search/?sort_by=&min_price=0&max_price=100&noprice=1&min_discount=0&max_discount=100&min_reviewsavg=10&max_reviewsavg=100&noreviews=1&available_in=FR&gametype=all&query=&page=1']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//div[@class="item force-badge"]/a']), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths=['//ul[@class="pagination bottom"]/li/a']),follow=True),
    )

    def parse_item(self, response):
        item = ItemLoader(item = InstantItem(), response=response)
        # item["Title"] = response.xpath('//div[@class = "infos mainshadow"]/h1/text()').extract_first()
        # item["Plateform"] = response.xpath('//div[@class = "subinfos"]/a/text()').extract()[1]
        # item["Release"] = response.xpath('//div[@class =  "release"]/span/text()').extract_first()
        # item["Tags"] = response.xpath('//div[@class = "tags"]/a/text()').extract()
        # item["Flat_price"] = response.xpath('//div[@class = "retail"]/span/text()').extract_first()
        # item["Discount"] = response.xpath('//div[@class = "discount"]/text()').extract_first()
        # price = response.xpath('//div[@class = "price"]/text()').extract()
        # if (isinstance(price,list)):
        #     item["Price"] = price[0]
        # else:
        #     item["Price"] = price
        # item["Developer"] = response.xpath('//div[@class =  "developer"]/a/text()').extract()
        # item["Publisher"] = response.xpath('//div[@class =  "publisher"]/a/text()').extract_first()
        

        item.add_xpath("Title", '//div[@class = "infos mainshadow"]/h1')
        item.add_xpath("Plateform",'//div[@class = "subinfos"]/a')
        item.add_xpath("Release",'//div[@class =  "release"]/span')
        item.add_xpath("Tags", '//div[@class = "tags"]/a')
        item.add_xpath("Flat_price", '//div[@class = "retail"]/span')
        item.add_xpath("Discount",'//div[@class = "discount"]')
        item.add_xpath("Price", '//div[@class = "price"]')
        item.add_xpath("Developer", '//div[@class =  "developer"]/a')
        item.add_xpath("Publisher", '//div[@class =  "publisher"]/a')
        return item.load_item()