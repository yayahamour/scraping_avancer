
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from g2a_scraping.items import G2AScrapingItem

class G2aSpider(CrawlSpider):
    name = 'g2a'
    allowed_domains = ['g2a.com']
    start_urls = ['https://www.g2a.com/category/games-c189']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=['//li[@class = "indexes__ProductCardStyledWrapper-wklrsw-118 indexes__ProductCardBigStyledWrapper-wklrsw-119 dJMasQ ejjnIN pc-digital pc-hover"]/div/a']), callback='parse_item', follow=True),
        #Rule(LinkExtractor(restrict_xpaths=['//nav[@class = "indexes__StyledNavigation-wklrsw-73 fExopu"]/ul/li/a']),follow=True),
     )
    def parse_item(self, response):
        item = G2AScrapingItem()
        item["Title"] = response.xpath('//h1[@class ="indexes__StyledBaseTypography-wgki8j-99 indexes__StyledTypographyHeader-wgki8j-100 cmMwjF hZGKBs indexes__StyledTypography-wgki8j-111 iaCbpI"]/text()').extract_first()
        item["Plateform"] = response.xpath('//p[@class ="indexes__StyledAttributeValue-wgki8j-3 YNDRk"]/text()').extract()[0]
        item["Release"] = response.xpath('//p[@class ="indexes__StyledAttribute-sc-1vts47h-124 bYkoxP"]/b/text()').extract_first()
        tab = response.xpath('//div[@class = "indexes__PriceDetails-lqqtz4-39 aBrWG"]/span/text()').extract()
        item["Flat_price"] = tab[3]
        item["Discount"] = tab[12]
        item["Price"] = tab[8]
        yield item

