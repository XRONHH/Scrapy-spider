import requests
import os
import pymysql
import requests

# 建立商品1对应的缩略图片相册
# 输入一个商品分类，以及所有商品编号列表
# 返回路径：return all_path
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

# 获取我的数据库中的大图链接
# 输入需要执行的查询语句
# 返回所有图片组成的列表：return myimgurl
def getmyimgurl(sql):
    # myimgurls = []
    myimgurls = {}
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    cursor =conn.cursor()
    # sql_select = "select book_id, imgurl, category_id from book_info"
    cursor.execute(sql)
    # 数据库中大图链接
    myimgurl = cursor.fetchall()
    # print(myimgurl)
    # for url in myimgurl:
    #     print(url)
    #     for i in range(3):
    #         print("-------------------")
    #         print(url[i])
    # for imgurl in myimgurl:
    #     # myimgurls.append(imgurl[0])
    #     myimgurls['book_id'] = imgurl[0]
    #
    # print(myimgurls)
    # for url in myimgurls:
    #     print(url)
    print(myimgurl)
    return myimgurl            #元组
    # return myimgurls         #列表

# 获取数据库中的缩略图，并从网页中爬取到对应的图片，存入对应文件夹中
# 输入需要查询的sql语句，以及图书分类列表
# 执行成功返回0：return 0
def getdetailimg(sql, categorys):
    conn=pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    cursor=conn.cursor()
    # sql_select = "select img_id, img_url from book_detail"
    cursor.execute(sql)
    datas = cursor.fetchall()
    # 爬取缩略图准备工作
    books_imgs="\\books_imgs\\"
    base_path = os.getcwd() + books_imgs
    # 爬取的目录
    # categorys = ["java", "python"]
    for category in categorys:
        # 设置对应分类的路径
        path = base_path + "\\" + str(category)
        index = 1
        for data in datas:
            path_detail = path + "\\" + str(data[0])
            if os.path.isdir(path_detail):
                re = requests.get(data[1])
                filename = os.path.join(path_detail, str(index) + ".jpg")
                with open(filename, 'wb') as f:
                    f.write(re.content)
                index += 1
    return 0


# 查询数据库表中大致有哪几种分类,输入表名table
# 读取分类表
def getCategory(table):
    # 建立数据库连接
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    sql_select = "select category_id from" + table
    # 创建游标
    cursor = conn.cursor()
    # 执行查询
    cursor.execute(sql_select)
    datas = cursor.fetchall()
    category_ids = []
    for data in datas:
        category_ids.append(data[0])
    return category_ids

# 查询数据库中对应的book_id，
# 输入一个种类，根据种类查询book_id
# 输出一个ids列表存放所有的book_id，即所有图书编号列表：return ids
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


# 从网站中爬取图片，并完成编码存入对应的文件夹中
# 输入的myimgurls来源于我的数据库中的大图链接。
def getimg(myimgurl):
    index=1
    books_imgs = "\\books_imgs\\"
    base_path = os.getcwd() + books_imgs
    for url in myimgurl:
        print(url)
        imgurl = url[1]             # 需要爬取的imgurl
        book_id=url[0]              # 图片编号，用于定位
        category_id = url[2]        # 种类，用于定位
        re = requests.get(imgurl)
        # 1、首先需要定位到目标位置
        #path = 'F:\\graduation_project\\books_imgs\\imgs'
        path = base_path + "\\" + str(category_id) + "\\" + str(book_id)
        # 图片名称编码
        filename = os.path.join(path, str(book_id)+".jpg")
        print(filename)
        with open(filename, 'wb') as f:
            f.write(re.content)
        index += 1
    return 0

# 为每个文件夹下的缩略图重新命名
# 输入所有图书编号列表，一个种类
# 执行成功返回0
def newImgname(book_ids, category):
    books_imgs = "books_imgs"
    base_path = os.getcwd()+"\\"+books_imgs
    for book_id in book_ids:
        path = base_path + os.sep + category + os.sep + book_id
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

# ----------------------算法执行流程-----------------
# 1、 首先需要给定需要建立的分类
# categorys = ['python', 'java']
# 2、 按照book_id给图片库命名：getId(category),createPath(category,ids)
# for category in categorys:
#     print(category)
#     createPath(category, getId(category))
# 3、 获取数据库中的大图链接url，并对链接进行图片爬取，存入目标文件夹中：getmyimgurl(sql), getimg(myimgurl)
# for url in getmyimgurl():
#      print(url)
# sql_select = "select book_id, imgurl, category_id from book_info"
# getimg(getmyimgurl(sql_select))
# 4、 对缩略图进行爬取，并存入到对应的文件夹中:getdetailimg(sql,categorys)
# sql_select2 = "select img_id, img_url from book_detail"
# getdetailimg(sql_select2)
# 5、 对缩略图的文件名进行统一修改:newImgname(book_ids,category)
# category_ids = ["java", "python"]
# for category in categorys:
#     newImgname(getId(category),category)

