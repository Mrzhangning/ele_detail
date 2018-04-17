# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from ele.pymysqlpool import ConnectionPool
from ele import settings


class EleMysqlPipeline(object):

    def __init__(self):
        config = dict(
            pool_name='eleshop',
            host=settings.MYSQL_HOST,  # 读取settings中的配置
            port=settings.MYSQL_PORT,
            user=settings.MYSQL_USER,
            password=settings.MYSQL_PASSWD,
            database=settings.MYSQL_DBNAME,
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
        )
        self.pool = ConnectionPool(**config)

    def process_item(self, item, spider):
        with self.pool.cursor() as cursor:
            cursor.execute(
                "INSERT INTO ele_detail (poi_id, poi_name, poi_status, poi_addr, poi_phone, poi_rating, poi_open_hours, poi_rating_count, ord_num_month, poi_notice, min_delivery_price, shipping_fee, avg_speed, poi_img) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (item["poi_id"], item["poi_name"], item["poi_status"], item["poi_addr"],
                 item["poi_phone"],
                 item["poi_rating"], item["poi_open_hours"], item["poi_rating_count"], item["ord_num_month"], item["poi_notice"],
                 item["min_delivery_price"], item["shipping_fee"], item["avg_speed"], item["poi_img"]))

    def close_spider(self,spider):
        self.pool.close()





