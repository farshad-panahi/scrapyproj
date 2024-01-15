# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from w3lib.html import remove_tags
from itemloaders.processors import MapCompose, TakeFirst


# some inner funcs to use inside Multiple funcs in MapCompose
to_strip = lambda text: text.strip()
to_cap_letter = lambda text: text.capitalize()


class ProjectItem(scrapy.Item):
    country = scrapy.Field(input_processor=MapCompose(remove_tags, to_strip, to_cap_letter), output_processor=TakeFirst())
    capital = scrapy.Field(input_processor=MapCompose(remove_tags, to_strip), output_processor=TakeFirst())
    population = scrapy.Field(input_processor=MapCompose(remove_tags, to_strip), output_processor=TakeFirst())
    area = scrapy.Field(input_processor=MapCompose(remove_tags, to_strip), output_processor=TakeFirst())
 