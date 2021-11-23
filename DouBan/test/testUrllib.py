# coding=utf-8
import urllib.request
import urllib.parse
# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))


# post 
# 模拟用户登录时使用post
# data = bytes(urllib.parse.urlencode({'user': 'shuchenglin'}), encoding='utf-8')
# res = urllib.request.urlopen("http://httpbin.org/post", data=data)
# print(res.read().decode('utf-8'))

# 超时处理
# try:
#     res = urllib.request.urlopen("http://httpbin.org/get",timeout=3)
#     print(res.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print('time out')

# res = urllib.request.urlopen("http://www.baidu.com")
# print(res.status)
# print(res.getheaders())
url = 'https://www.douban.com'
data = bytes(urllib.parse.urlencode({"user":"AI"}), encoding='utf-8')
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
req = urllib.request.Request(url=url,data=data,headers=headers)
res = urllib.request.urlopen(req)
print(res.read().decode('utf-8'))
