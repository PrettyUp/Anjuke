# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AnjukeSZItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    loupan_id = scrapy.Field()
    loupan_name = scrapy.Field()
    loupan_status = scrapy.Field()
    loupan_price = scrapy.Field()
    loupan_discount = scrapy.Field()
    loupan_layout = scrapy.Field()
    loupan_location = scrapy.Field()
    loupan_opening = scrapy.Field()
    loupan_transfer = scrapy.Field()
    loupan_type = scrapy.Field()
    loupan_age = scrapy.Field()
    loupan_url = scrapy.Field()

class AnjukeSZSHItem(scrapy.Item):
    house_title = scrapy.Field()
    house_cost = scrapy.Field()
    house_code = scrapy.Field()
    house_public_time = scrapy.Field()
    house_community = scrapy.Field()
    house_location = scrapy.Field()
    house_build_years = scrapy.Field()
    house_kind = scrapy.Field()
    house_layout = scrapy.Field()
    house_size = scrapy.Field()
    house_face_to = scrapy.Field()
    house_point = scrapy.Field()
    house_price = scrapy.Field()
    house_first_pay = scrapy.Field()
    house_month_pay = scrapy.Field()
    house_decorate_type = scrapy.Field()
    house_agent = scrapy.Field()
    house_agency = scrapy.Field()
    house_url = scrapy.Field()
