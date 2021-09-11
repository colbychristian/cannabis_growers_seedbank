import scrapy
import logging

class SeedbankSpider(scrapy.Spider):
    name = 'seedbank'
    #allowed_domains = ['https://growdiaries.com/']
    start_urls = ['https://growdiaries.com/seedbank/']

    def parse(self, response):
        rows = response.xpath("//a[@class='breeder_item rating_list ']")
        for row in rows:
            sub_link = row.xpath(".//@href").get()
            link = sub_link + "/strains"

            yield response.follow(url=link, callback=self.parse_strain)

    #def parse_breeder(self, response):
        #rows = response.xpath("//div[@class='tabs touch_slider_content']/a[6]")
        #for row in rows:
            #link = row.xpath(".//@href").get()

            #yield response.follow(url=link, callback=self.parse_strain)

    def parse_strain(self, response):
        rows = response.xpath("//a[@class='seed']")
        for row in rows:
            link = row.xpath(".//@href").get()

            yield response.follow(url=link, callback=self.parse_attributes)

    def parse_attributes(self, response):
        rows = response.xpath("//body[@id='body_page']")
        for row in rows:
            breeder = row.xpath(".//div[@class='name_bank']/a/text()").get()
            strain = row.xpath(".//h1[@class='name']/span/text()").get()
            grow_score = row.xpath(".//div[@class='item rate_value']/div[@class='value']/span[1]/text()").get()
            description = row.xpath(".//div[@class='text more_less']/text()").get()
            description2 = row.xpath(".//div[@class='text more_less']/p/text()").get()
            gender = row.xpath(".//div[@class='params']/div[1]/span[3]/text()").get()
            gender2 = row.xpath(".//div[@class='params']/div[1]/span[4]/text()").get()
            genes = row.xpath(".//div[@class='params']/div[2]/span[3]/text()").get()
            genetics = row.xpath(".//div[@class='params']/div[3]/span[3]/text()").get()
            genetics2 = row.xpath(".//div[@class='params']/div[2]/span[3]/text()").get()
            harvest = row.xpath(".//div[@class='params']/div[4]/span[3]/text()").get()
            harvest2 = row.xpath(".//div[@class='params']/div[3]/span[3]/text()").get()
            flowering = row.xpath(".//div[@class='params']/div[5]/span[3]/text()").get()
            flowering2 = row.xpath(".//div[@class='params']/div[4]/span[3]/text()").get()
            THC = row.xpath(".//div[@class='params']/div[6]/span[3]/text()").get()
            THC2 = row.xpath(".//div[@class='params']/div[5]/span[3]/text()").get()
            CBD = row.xpath(".//div[@class='params']/div[8]/span[3]/text()").get()
            CBD2 = row.xpath(".//div[@class='params']/div[7]/span[3]/text()").get()
            vegetation = row.xpath(".//div[@class='params']/div[9]/span[3]/text()").get()

            yield {
                'breeder': breeder,
                'strain': strain,
                'grow_score': grow_score,
                'description': description,
                'description2': description2,
                'gender': gender,
                'gender2': gender2,
                'genes': genes,
                'genetics': genetics,
                'genetics2': genetics2,
                'harvest': harvest,
                'harvest2': harvest2,
                'flowering': flowering,
                'flowering2': flowering2,
                'THC': THC,
                'THC2': THC2,
                'CBD': CBD,
                'CBD2': CBD2,
                'vegetation': vegetation
            } 
