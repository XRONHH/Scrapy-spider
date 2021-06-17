
def analyze_json(jsons):
    """
    解析传进来的jsons,将jsons解析成key-value并输出
    :param jsons: 需要解析的json字符串
    :return:
    """
    key_value=''
    # isinstance函数是Python的内部函数，他的作用是判断jsons这个参数是否为dict类型
    # 如果是的话返回True，否则返回False
    if isinstance(jsons, dict):
        for key in jsons.keys():
            key_value=jsons.get(key)
            if isinstance(key_value, dict):
                analyze_json(key_value)
            elif isinstance(key_value, list):
                for json_array in key_value:
                    analyze_json(json_array)
            else:
                print(str(key)+" = "+str(key_value))
    elif isinstance(jsons, list):
        for json_array in jsons:
            analyze_json(json_array)


def output_value(jsons, key):
    """
    通过参数key，在jsons中进行匹配并输出该key对应的value
    :param jsons: 需要解析的json串
    :param key: 需要查找的key
    :return:
    """
    key_value=''
    if isinstance(jsons, dict):
        for json_result in jsons.values():
            if key in jsons.keys():
                key_value=jsons.get(key)
            else:
                output_value(json_result, key)
    elif isinstance(jsons, list):
        for json_array in jsons:
            output_value(json_array, key)
    if key_value != '':
        print(str(key)+" = "+str(key_value))


# 定义一个jsons1串
jsons1={"b": {"a": [{"n1": "WIFI", "lo": 116.30744414106923, "t2": "1387873418.195T+08:00", "t3": "target_首页-海报视频点击",
                     "p1": "com.tudou.ui.activity.HomeActivity", "n2": 840, "la": 39.98049465154441, "l": False},
                    {"n1": "WIFI", "lo": 116.30744414106923, "t2": "1387873415.880T+08:00", "t1": "A1005", "s1":
                        "5da19f89080af666bc2cb8d8775706df", "p1": "com.tudou.ui.activity.HomeActivity"}]},
        "h": {"i": {"o2": "4.3", "o1": "Android", "b2": "Nexus 7", "m": "10:bf:48:c2:81:f5", "h": 1205, "w":
            800, "u": "f835c7f8-c331-4b47-a6a3-772021544aa9", "b1": "google"}}}
# 调用解析
jsons2 = open('comment.txt','r')
print('将jsons1解析后的结果如下：')
analyze_json(jsons2)
# 调用查找
print('…………………………………………………………………………')
print('查找jsons1中t2key的value值如下')
output_value(jsons2, 'html')