# -*- coding: utf-8 -*-

from scrapy.spiders import Spider
from scrapy_splash import SplashRequest
from ele.items import ProxyIPItem


class XiciSpider(Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = [
        "http://www.xicidaili.com/nn",
        "http://www.xicidaili.com/nn/2",
        "http://www.xicidaili.com/nn/3",
        "http://www.xicidaili.com/nn/4",
        "http://www.xicidaili.com/nn/5",
        "http://www.xicidaili.com/nn/6",
        "http://www.xicidaili.com/nn/7",
        "http://www.xicidaili.com/nn/8",
        "http://www.xicidaili.com/nn/9",
        "http://www.xicidaili.com/nn/10"
    ]

    # request需要封装成SplashRequest
    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': '0.5'}
                                )

    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]/tbody/tr')
        for ip in ip_list:
            item = ProxyIPItem()
            item['ip'] = ip.xpath('td[2]/text()').extract()[0]
            item['port'] = ip.xpath('td[3]/text()').extract()[0]
            item['type'] = ip.xpath('td[6]/text()').extract()[0]
            print(item)
            yield item
