import scrapy
from scrapy.loader import ItemLoader

from project.items import ProjectItem


class ThegodfotherSpider(scrapy.Spider):
    name = "theGodFother"
    # allowed_domains = ["en.wikipedia.org"]
    start_urls = ["https://www.scrapethissite.com/pages/simple/"]

    def parse(self, response):

        for country in response.css('div.country'):
            ins = ItemLoader(item=ProjectItem(), selector=country)
            
            ins.add_css('country', 'h3.country-name')
            ins.add_css('capital', 'span.country-capital::text')
            ins. add_css('population', 'span.country-population::text')
            ins.add_css('area', 'span.country-area::text')
            
            yield ins.load_item() 