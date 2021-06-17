import os
import pymysql

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

# 为每个文件夹下的缩略图重新命名
def newImgname(book_ids, category_id):
    books_imgs = "books_imgs"
    base_path = os.getcwd()+"\\"+books_imgs
    for book_id in book_ids:
        path = base_path + os.sep + category_id + os.sep + book_id
        index = 0
        n = 1
        filelist = os.listdir(path)
        jpg = ".jpg"
        for i in filelist:
            oldname = path + os.sep + filelist[index]  # 文件名
            bigname = path + os.sep + book_id + jpg  # 大图文件名
            newname = path + os.sep + str(n) + jpg  # 新命名
            if not oldname == bigname:
                os.rename(oldname, newname)
                n += 1
                index += 1
                print(oldname, newname, n)
    return 0

category_ids = ["java", "python"]
for category_id in category_ids:
    newImgname(getId(category_id),category_id)

# books_imgs = "books_imgs"
# base_path = os.getcwd() + "\\" + books_imgs
# cate_name = "java"
# book_id = "p9265169"
#
# path = base_path + "\\"+ cate_name + "\\" +book_id
#
# index = 0
# n = 1
# filelist = os.listdir(path)
# jpg = ".jpg"
# for i in filelist:
#     oldname = path + os.sep + filelist[index]    #文件名
#     bigname = path + os.sep + book_id + jpg      #大图文件名
#     newname = path + os.sep + str(n) + jpg       #新命名
#     if not oldname == bigname:
#         os.rename(oldname, newname)
#         n += 1
#         index += 1
#         print(oldname,newname,n)
#
# print(filelist)


