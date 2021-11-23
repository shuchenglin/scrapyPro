import re


a_list = ["123@qq.com", "123@126.com", "@163.com", "@.com" ,"123@huawei.com"]

# 创建规则对象
# pat = re.compile(".*@qq.com")

# for a in a_list:
    # match 方法，进行匹配
    # if re.match(".*@qq.com", a):  # 前面是规则模板，后面是校验对象
    #     print(a)
    # search 方法
    # if re.search(".*@qq.com", a):
    # findAll() 方法
    # if re.findall(".*@qq.com", a):
    #     print(a)

# findall()
# print (re.findall("[A-Z]+", "AbCdEf"))

# sub()
print(re.sub('a', 'A', r'aAbCa'))


#在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
a = r"\aabd-\'"
print(a)