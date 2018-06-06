# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class AnjukeSZPipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "anjuke", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "insert into sz_loupan_info(loupan_name,loupan_status,loupan_price,loupan_discount,loupan_layout,loupan_location,loupan_opening,loupan_transfer,loupan_type,loupan_age,loupan_url)\
               values('%s','%s','%d','%s','%s','%s','%s','%s','%s','%s','%s')"\
               %(item['loupan_name'],item['loupan_status'],int(item['loupan_price']),item['loupan_discount'],item['loupan_layout'],item['loupan_location'], \
                 item['loupan_opening'],item['loupan_transfer'],item['loupan_type'],item['loupan_age'],item['loupan_url'])
        self.cursor.execute(sql)
        self.db.commit()
        return item

    def __del__(self):
        self.db.close()


class AnjukeSZSHPipeline(object):
    def __init__(self):
        self.db = pymysql.connect("localhost", "root", "root", "anjuke", charset="utf8")
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = "insert into sz_sh_house_info(house_title,house_cost,house_code,house_public_time,house_community,house_location,house_build_years,house_kind,house_layout,house_size,\
               house_face_to,house_point,house_price,house_first_pay,house_month_pay,house_decorate_type,house_agent,house_agency,house_url)\
               values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"\
               %(item['house_title'],item['house_cost'],item['house_code'],item['house_public_time'],item['house_community'],item['house_location'],\
                 item['house_build_years'],item['house_kind'], item['house_layout'],item['house_size'],item['house_face_to'],item['house_point'],item['house_price'],\
                 item['house_first_pay'],item['house_month_pay'],item['house_decorate_type'],item['house_agent'],item['house_agency'],item['house_url'])
        self.cursor.execute(sql)
        self.db.commit()
        return item

    def __del__(self):
        self.db.close()
