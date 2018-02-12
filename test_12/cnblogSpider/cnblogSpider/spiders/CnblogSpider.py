# coding:utf-8
import scrapy
class CnblogSpider(scrapy.Spider):
    name = "cnblogs"
    start_urls = [
      "http://www.cnblogs.com/qiyeboy/default.html?page=1"
    ]
    def parse(self,response):
        print(response)

