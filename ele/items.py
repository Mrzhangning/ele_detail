# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ProxyIPItem(scrapy.Item):
    ip = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()



class EleShopItem(scrapy.Item):
    # 商家ID
    poi_id = scrapy.Field()
    # 商家名称
    poi_name = scrapy.Field()
    # 商家状态
    poi_status = scrapy.Field()
    # 商家地址
    poi_addr = scrapy.Field()
    # 商家电话
    poi_phone = scrapy.Field()
    # 评分
    poi_rating = scrapy.Field()
    # 营业时间
    poi_open_hours = scrapy.Field()
    # 评分人数
    poi_rating_count = scrapy.Field()
    # 月销量
    ord_num_month = scrapy.Field()
    #商家公告
    poi_notice = scrapy.Field()
    # 起送价
    min_delivery_price = scrapy.Field()
    # 配送费
    shipping_fee = scrapy.Field()
    # 平均配送时间
    avg_speed = scrapy.Field()
    # 商家图片
    poi_img = scrapy.Field()


