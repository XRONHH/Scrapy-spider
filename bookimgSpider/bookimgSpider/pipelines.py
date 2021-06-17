# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt

class BookimgspiderPipeline(object):
    # 将数据存入到xls表格中
    def __init__(self):
        self.filename="当当图片信息.xls"
        self.book = xlwt.Workbook(encoding="utf8")
        self.sheet=self.book.add_sheet('图书信息', cell_overwrite_ok=True)

        heads=['编号', '标题', '图片', '介绍', '价格', '作者']
        for head in heads:
            self.sheet.write(0, heads.index(head), head)
        self.line = 1

    def process_item(self, item, spider):
        j=0
        for k, v in item.items():
            if k == "price":
                v="".join(v)
            self.sheet.write(self.line, j, v)
            j+=1
        self.line+=1
        return item

    def close_spider(self, spider):
        self.book.save(self.filename)
