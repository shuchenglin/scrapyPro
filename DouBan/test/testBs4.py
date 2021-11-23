from bs4 import BeautifulSoup
import re
'''
BeautifulSoup将复杂HTML文档转换成一个复杂的树形结构，每个节点都是python对象
'''

file = open("DouBan/test/baidu.html", 'rb')
html = file.read().decode()

bs = BeautifulSoup(html, "html.parser")

# 打印标签中的内容
# print(bs.title.string)
# print(bs.a)

# ---------------------------------------------
# 遍历文档
# print(bs.div.contents[1])

# 文档搜索
# 1.findall()
# a_list = bs.find_all('a')

# 2.正则表达式搜索， search()
# a_list = bs.find_all(re.compile("a"))

# 3.方法：传入一个函数，根据函数的要求来搜索
# def name_is_exist(tag):
#     return tag.has_attr("class")

# a_list = bs.find_all(name_is_exist)


#4. css选择器
# a_list = bs.select('head > title')

a_list = bs.select(".mnav ~ .test")
# for item in a_list:
#     print(item)
# print(a_list)
print(a_list[0].get_text())