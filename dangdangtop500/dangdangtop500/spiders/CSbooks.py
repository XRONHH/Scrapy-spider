# -*- coding: utf-8 -*-
import scrapy
import time

class CsbooksSpider(scrapy.Spider):
    name = 'CSbooks'
    allowed_domains = ['bang.dangdang.com']
    # start_urls = ['http://bang.dangdang.com/']
    # 24小时计算机/网络榜: http://bang.dangdang.com/books/bestsellers/01.54.00.00.00.00-24hours-0-0-1-1
    start_urls = []
    url1 = "http://bang.dangdang.com/books/bestsellers/01.54.00.00.00.00-24hours-0-0-1-"
    index = 1
    for index in range(26):
        start_urls.append(url1 + str(index))
    print(start_urls)
    def parse(self, response):

        divs = response.xpath('.//div[@class="bang_list_box"]/ul[1]/li')

        for div in divs:
            item = {}
            item['name'] = div.xpath('./div[@class="name"]/a/text()').extract_first()
            item['commentCount'] = div.xpath('./div[@class="star"]/a/text()').extract_first()
            item['author'] = div.xpath('./div[@class="publisher_info"][1]/a[1]/@title').extract_first()
            item['publish_date'] = div.xpath('./div[@class="publisher_info"][2]/span[1]/text()').extract_first()
            item['publisher'] = div.xpath('./div[@class="publisher_info"][2]/a/text()').extract_first()
            item['price_n'] = div.xpath('./div[@class="price"]/p[1]/span[1]/text()').extract_first()
            item['price_r'] = div.xpath('./div[@class="price"]/p[1]/span[2]/text()').extract_first()
            item['price_s'] = div.xpath('./div[@class="price"]/p[1]/span[3]/text()').extract_first()
            # time.sleep(1)
            print(item)
            yield item

