# -*- coding: utf-8 -*-
import scrapy

from scrapy_splash import SplashRequest
from ele.items import EleShopItem
from ele.shoplist import get_shopid_list
import json


class EleshopSpider(scrapy.Spider):
    name = "eleshop"
    allowed_domains = ["www.ele.me/shop"]

    #website_possible_httpstatus_list = [403]
    #handle_httpstatus_list = [403]

    def start_requests(self):
        shop_list = get_shopid_list()
        #start_url = "https://www.ele.me/restapi/shopping/restaurant"
        #"https://www.ele.me/restapi/shopping/restaurant/161360187?&terminal=pc"
        urls = ['https://www.ele.me/restapi/shopping/restaurant/{}?&terminal=pc'.format(i) for i in shop_list]

        for url in urls:
            # http://112.86.73.52:53281
            # yield SplashRequest(url=url, callback=self.parse,args={"wait":0.5},headers = {'Content-Type': 'application/json'})
            yield scrapy.Request(url=url, callback=self.parse,)

    def parse(self, response):
        if response.body == "banned":
            req = response.request
            req.meta["change_proxy"] = True
            yield req
        else:
            data = response.text
            jdata = json.loads(data)
            item = EleShopItem()
            item['poi_id'] = jdata['id']     #poi_id
            item['poi_name'] = jdata['name']  #poi_name
            item['poi_status'] = jdata['status'] #poi_status  状态：4-商家休息   1-在线  5-预定中状态
            item['poi_addr'] = jdata['address'] #poi_addr
            item['poi_phone'] = jdata['phone']   #电话
            item['poi_rating'] = jdata['rating']  #poi_rating  评分
            item['poi_open_hours']=jdata['opening_hours']  #营业时间
            item['poi_rating_count'] = jdata['rating_count'] #poi_rating_count #评分人数
            item['ord_num_month'] = jdata['recent_order_num']  #ord_num_month 月销量
            item['poi_notice'] = jdata['promotion_info']   #poi_notice 商家公告
            item['min_delivery_price'] = jdata['float_minimum_order_amount']  # 起送价
            item['shipping_fee'] = jdata['float_delivery_fee'] #  shipping_fee配送费
            item['avg_speed'] = jdata['order_lead_time']  # 平均配送时间
            item['poi_img'] = jdata['image_path']  #poi_img 商家图片


            yield item
