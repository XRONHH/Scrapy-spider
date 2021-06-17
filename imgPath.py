import pymysql
import os
import re


# 连接本地数据库，并完成sql操作
# 输入需要执行的sql语句，返回结果。
# cursor.fetchall()返回的数据类型为元组
def myDB(sql):
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

# 获取数据库中商品的相关信息
# 返回book_id, category_id
def getBookinfo():
    book_ids = []
    category_ids = []
    # 建立数据库连接
    # 1、获取链接
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    # 2、初始化游标
    cursor = conn.cursor()
    # 3、进行数据库操作
    sql_select = "select book_id,category_id from book_info"
    cursor.execute(sql_select)
    ids = cursor.fetchall()
    for id in ids:
        book_ids.append(id[0])
        category_ids.append(id[1])
        print(id)
    print(book_ids, category_ids)
    # 返回一个包含两个list的
    return book_ids, category_ids

# 生成商品详细页面,并放到我的数据库中
def crateUrl(imgids):
    urls = []
    book_ids = imgids[0]
    category_ids = imgids[1]
    for book_id in book_ids:
            s = re.findall("\d+", book_id)[0]
            print("--------------------------", s)
            urls.append('http://product.dangdang.com/' + s + ".html")
    print(urls)
    print(book_ids)
    print(category_ids)
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    cursor = conn.cursor()
    for index in range(len(book_ids)):
        cursor.execute("insert into book_img(book_id, imgurl, category_id)value ('{}','{}','{}')".format(book_ids[index],urls[index],category_ids[index]))
        conn.commit()
    return 0
# print(getBookinfo()[0])
crateUrl(getBookinfo())
