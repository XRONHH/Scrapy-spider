import urllib
import requests
import re
import pymysql

# 获取详情页面的缩略图
def getDetilimg():
    # 从数据库中取出详情页面信息
    conn = pymysql.connect("localhost", "root", "123456", "goods", charset="utf8")
    cursor = conn.cursor()
    sql_select = "select book_id,imgurl,category_id from book_img"
    cursor.execute(sql_select)
    datas = cursor.fetchall()
    for data in datas:
        print(data)
        print(data[0])
    print(datas)
    return 0

# 利用re正则表达式爬取页面图片
# def getHtml(url):
#     page = urllib.urlopen(url)
#     html = page.read()
#     return html
#
# def getImg(html):
#     reg = 'src="(.+?\.jpg)" alt='
#     imgre = re.compile(reg)
#     imglist = re.findall(imgre, html)
#     index = 0
#     for imgurl in imglist:
#         urllib.urlretrieve(imgurl, '%s.jpg'%index)
#         index +=1
#     return imglist

getDetilimg()
