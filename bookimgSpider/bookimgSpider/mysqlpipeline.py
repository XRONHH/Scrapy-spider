# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import xlwt

import pymysql

class MysqlPipeline(object):
    # 将数据存入到mysql数据库中
    def __init__(self):
        # 建立连接
        self.conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
        # 创建游标
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # sql语句
        # insert_sql = "insert into book_info(title, name, price, author) VALUES (%s, %s, %s, %s)"
        # self.cursor.executemany(insert_sql, (item['title'], item['name'], item['price'], item['author']))
        # self.cursor.executemany(insert_sql, ("1", "2", "3", item['author']))
        self.cursor.execute('insert into book_detail(img_id,img_url)VALUES ("{}","{}")'
                            .format(item['img_id'], item['img_url']))
        self.conn.commit()

    def close_spider(self, spider):
        # 关闭连接
        self.cursor.close()
        self.conn.close()
