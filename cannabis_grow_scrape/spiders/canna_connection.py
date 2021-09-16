import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CannaConnectionSpider(CrawlSpider):
    name = 'canna_connection'
    allowed_domains = ['www.cannaconnection.com']
    start_urls = ['http://www.cannaconnection.com/strains/breeders']

    rules = (
        Rule(LinkExtractor(restrict_xpaths = "//ul[@class='list']/li/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths = "//div[@class='post-list-row']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths = "//li[@id='pagination_next_bottom']/a"), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths = "//li[@id='pagination_next']/a"), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            'name': response.xpath("//div[@class='primary_block post-content ']/h1/text()").get(),
            'breeder': response.xpath("normalize-space(//div[@class='breeder-name']/text())").get(),
            'description': response.xpath("normalize-space(//div[@class='rte']/p/text())").get(),
            'genetics': response.xpath("normalize-space((//div[@class='feature-value'])[1]/text())").get(),
            #'parents': response.xpath("").get(),
            'THC': response.xpath("normalize-space((//div[@class='feature-value'])[2]/text())").get(),
            'CBD': response.xpath("normalize-space((//div[@class='feature-value'])[3]/text())").get(),
            #'smell_and_flavour': response.xpath("").get(),
            #'effect': response.xpath("").get(),
            'grow_difficulty': response.xpath("normalize-space((//dl[@class='data-sheet'])[1]/dd[1]/text())").get(),
            'flowering_type': response.xpath("normalize-space((//dl[@class='data-sheet'])[1]/dd[2]/text())").get(),
            'flowering_time': response.xpath("normalize-space((//dl[@class='data-sheet'])[1]/dd[3]/text())").get(),
            'outdoor_harvest_time': response.xpath("normalize-space((//dl[@class='data-sheet'])[1]/dd[4]/text())").get(),
            'indoor_yield': response.xpath("normalize-space((//dl[@class='data-sheet'])[2]/dd[1]/text())").get(),
            'outdoor_yield': response.xpath("normalize-space((//dl[@class='data-sheet'])[2]/dd[2]/text())").get(),
            'indoor_height': response.xpath("normalize-space((//dl[@class='data-sheet'])[2]/dd[3]/text())").get(),
            'outdoor_height': response.xpath("normalize-space((//dl[@class='data-sheet'])[2]/dd[4]/text())").get()
        }
