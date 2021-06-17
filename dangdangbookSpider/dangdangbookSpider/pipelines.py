# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt

class DangdangbookspiderPipeline(object):
    # # 将数据存入到mysql数据库中
    # def __init__(self):
    #     # 建立连接
    #     self.conn = pymysql.connect("localhost", "root", "123456", "test", charset="utf8")
    #     # 创建游标
    #     self.cursor = self.conn.cursor()
    #
    # def process_item(self, item, spider):
    #     # sql语句
    #     insert_sql = """
    #     insert into book_info(title, name, price, author) VALUES (%s, %s, %s, %s)
    #     """
    #     self.cursor.executemany(insert_sql, (item['title'], item['name'], item['price'], item['author']))
    #     self.conn.commit()
    #
    # def close_spider(self, spider):
    #     # 关闭连接
    #     self.cursor.close()
    #     self.conn.close()

    # 将数据存入到xls表格中
    def __init__(self):
        self.filename="当当图书信息.xls"
        self.book = xlwt.Workbook(encoding="utf8")
        self.sheet=self.book.add_sheet('图书信息', cell_overwrite_ok=True)

        heads=['编号', '书名', '图片链接', '介绍', '价格', '作者']
        for head in heads:
            self.sheet.write(0, heads.index(head), head)
        self.line=1

    def process_item(self, item, spider):
        j=0
        for k, v in item.items():
            if k == "price":
                v="".join(v)
            self.sheet.write(self.line, j, v)
            j += 1
        self.line += 1
        return item

    def close_spider(self, spider):
        self.book.save(self.filename)
