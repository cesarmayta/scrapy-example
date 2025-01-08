import scrapy


class WorldometersSpider(scrapy.Spider):
    name = "worldometers"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    def parse(self, response):
        # simple extraction
        title = response.xpath('//h1/text()').get()
        # example 1 - basic
        countries = response.xpath('//td/a/text()').getall()
        yield {
            'titles': title,
            'countries': countries,
        }
       
        
        
        
        
