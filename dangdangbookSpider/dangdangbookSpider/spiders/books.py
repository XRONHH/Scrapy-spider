# -*- coding: utf-8 -*-
import scrapy

# 爬取搜索到的主题书籍：如关键词（python，java...)
class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['dangdang.com']
    keyword = ["python", "java"]
    # start_urls = ['http://search.dangdang.com/?key=python&act=input',
    #               'http://search.dangdang.com/?key=python&act=input&page_index=2'
    # ]

    start_urls = []
    # for k in keyword:
    #     for i in range(2):
    #         start_urls[] = 'http://search.dangdang.com/?key=' + k + '&act=input&page_index=1'
    #         start_urls[1] = 'http://search.dangdang.com/?key=' + k + '&act=input&page_index=2'
    for k in keyword:
        for i in range(1, 2):
            start_urls.append('http://search.dangdang.com/?key=' + k + '&act=input&page_index=' + str(i))
    print(start_urls)
    def parse(self, response):
        divs = response.xpath('.//div[@class="con shoplist"]/div/ul/li')

        for div in divs:
            item = {}
            item['book_id'] = div.xpath('./@id').extract_first()
            item['book_name'] = div.xpath('./a/@title').extract_first()
            item['imgUrl'] = div.xpath('./a/img/@src').extract_first()
            if item['imgUrl'] == "images/model/guan/url_none.png":
                item['imgUrl'] = div.xpath('./a[@class="pic"]/img/@data-original').extract_first()
            item['detail'] = div.xpath('./p[1]/a/@title').extract_first()
            item['price'] = div.xpath('./p[3]/span/text()').extract()
            item['author'] = div.xpath('./p[5]/span/a[1]/text()').extract_first()
            # if self.k == "python":
            #     item['category_id'] = self.keyword[0]
            # elif self.k == "java":
            #     item['category_id'] = self.keyword[1]
            item['category_id'] = response.xpath('/html/head/meta[3]/@content').extract_first()
            print(item, type(item))
            print(item['book_id'])
            yield item

#http://product.dangdang.com/23997502.html
