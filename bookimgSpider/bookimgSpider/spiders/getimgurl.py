# -*- coding: utf-8 -*-
import scrapy
import pymysql
import re

# 获取图片链接
class GetimgurlSpider(scrapy.Spider):
    name = 'getimgurl'
    allowed_domains = ['product.dangdang.com']
    # 从数据库中获取书籍的book_id，用于生成商品详情页
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    cursor = conn.cursor()
    # sql_select = "select book_id from book_info"
    sql_select = "select book_id,category_id from book_info"
    cursor.execute(sql_select)
    book_ids = cursor.fetchall()
    ids = []        #图片编号
    categories =[]  #图片种类

    index = 0
    # print(book_ids)
    for book_id in book_ids:
        ids.append(book_id[0])
        categories.append(book_id[1])
    # print(book_ids)
    # 构造爬取的url
    # http://product.dangdang.com/23997502.html
    # start_urls = ['http://product.dangdang.com/']
    start_urls = []
    for id in ids:
        # 由于id的格式是p23997502，所以需要对字符串进行处理
        s = re.findall("\d+", id)[0]
        # 生成需要爬取的商品详情页
        start_urls.append('http://product.dangdang.com/' + s + ".html")
    # print("----------------"+start_urls)
    def parse(self, response):
        divs = response.xpath('.//div[@class="dp_slide_box"]/ul/li')
        for div in divs:
            item = {}
            item['img_url'] = div.xpath('./a/img/@src').extract_first()
            if item['img_url'] == "images/model/guan/url_none.png":
                item['img_url'] = div.xpath('./a/@data-imghref').extract_first()
            # item['category'] = response.xpath('/html/body/div[2]/div[2]/a[4]/text()').extract()
            # item['category_id'] = self.categories[self.index]
            # item['book_id'] = self.ids[self.index]
            # self.index += 1
            s = response.xpath('/html/head/link[1]/@href').extract_first()
            book_id = re.findall("\d+", s)[0]
            item['img_id'] = "p" + book_id
            print("---------------------------------")
            print(item)
            yield item

