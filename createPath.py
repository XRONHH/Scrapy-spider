import os
import pymysql
import requests

# 建立商品1对应的缩略图片相册，返回路径
def createPath(category, ids):
    # path1对应于当前py文件下的路径
    path1 = os.getcwd()
    all_path = []
    #print(path1)
    for id in ids:
        # 统一使用books_imgs作为图片存放根文件夹
        # 首先判断是否存在books_imgs文件夹，不存在则建立
        if not os.path.exists(path1 + '\\books_imgs'):
            os.mkdir(path1 + '\\books_imgs')
        books_imgs = "\\"+"books_imgs" + "\\"
        # path由当前路径、图片根文件夹、物品名关键字、物品id
        path = path1 + books_imgs + category + "\\" + id
        #print(path)
        # 建立获取到的所有图片编码的文件夹路径：./books_imgs/p31432423
        # 建立多个文件夹，使用makedir()
        os.makedirs(path)
        all_path.append(path)
    print(all_path)
    print("---------------------------")
    # 返回一个path列表，存放所有的图片链接
    return all_path

# 查询数据库中对应的book_id，输出一个ids列表存放所有的book_id
# 根据种类查询book_id
def getId(category):
    # 打开数据库，建立连接
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    # 查询表中，种类为category的书籍的book_id
    sql_select = "select book_id from book_info where category_id= '%s'"%category
    # 创建游标
    cursor = conn.cursor()
    # 执行查询
    cursor.execute(sql_select)
    book_ids = cursor.fetchall()
    ids = []
    for book_id in book_ids:
        ids.append(book_id[0])
    print(ids)
    return ids


# 根据图片的链接对图片进行爬取，并根据图片的路径存入对应的文件夹中
# 函数输入图片链接、图片路径、图片book_id
def imgSpider(imgurl, book_ids, category):
    books_imgs = "\\books_imgs"
    # 得到图片库根路径
    base_path = os.getcwd() + books_imgs
    # 遍历取出id

    return 0



category = ['python', 'java']
for name in category:
    print(name)
    createPath(name, getId(name))

