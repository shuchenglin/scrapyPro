# coding=utf-8
import sys
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3

'''
流程
1.爬取网页
2.解析数据
3.保存数据
'''

def main():
    # 目标网站
    baseurl = "https://movie.douban.com/top250?start="
    datalist = getData(baseurl)
    


    # savePath = u'DouBan/data/Douban_Movie_250.xls'
    # save data
    dbpath = 'test.db'
    saveDataDB(datalist, dbpath)
    #askURL(baseurl)
    print('爬取成功！！！')

# 创建正则表达式对象
# 超链接的规则
findLink = re.compile(r'<a href="(.*?)">')
# 影片图片链接
findImg = re.compile(r'<img.*src="(.*?)"',re.S)  # re.S 让换行符包含在字符中
# 影片名规则
findName = re.compile(r'<span class="title">(.*)</span>')
# 影片评分规则
findScore = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
# 影片评价人数规则
findPeople = re.compile(r'<span>(\d*)人评价</span>')
# 影片概述规则
findInq = re.compile(r'<span class="inq">(.*)</span>')
# 影片相关规则
findBd = re.compile(r'<p class="">(.*?)</p>', re.S)

# get page
def getData(baseurl):
    datalist = []
    # 调用获取页面信息的函数10次
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = askURL(url)
    
        # 解析数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_= "item"):
            data = []   # 保存一部电影的所有信息
            item = str(item)
            link = re.findall(findLink, item)[0]
            data.append(link)
            img = re.findall(findImg,item)[0]
            data.append(img)
            name = re.findall(findName, item)
            if len(name) == 2:
                cname = name[0]
                data.append(cname)
                ename = name[1].replace("/","")
                data.append(ename)
            else:
                data.append(name[0])
                data.append(' ')
            score = re.findall(findScore, item)[0]
            data.append(score)
            people = re.findall(findPeople,item)[0]
            data.append(people)
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)
            else:
                data.append(' ')
            about = re.findall(findBd, item)[0]
            about = re.sub('br(\s+)?/>(\s+)?','',about)  # 替换br
            about = re.sub('/', '', about) # 替换/
            data.append(about.strip())

            datalist.append(data)

    return datalist

# 得到一个指定的url的网页内容
def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发消息
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36"
    }
    req = urllib.request.Request(url,headers=head)
    html = ""
    try:
        res = urllib.request.urlopen(req)
        html = res.read().decode('utf-8')
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e, 'code'):
            print(e.code)
        if hasattr(e, 'reason'):
            print(e.reason)
    return html

# save data
def saveData(datalist, savepath):
    # 创建一个execl对象
    book = xlwt.Workbook(encoding='utf-8', style_compression= 0)
    # 创建一个sheet表
    sheet = book.add_sheet('豆瓣电影250', cell_overwrite_ok= True)
    # 创建列名
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外文名', '评分', '评价数', '概况', '相关信息')
    # 把列名写入第一行
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    
    # 把爬取到的内容写入表格
    for i in range(0,250):
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i+1, j, data[j])
    
    # 保存execl
    book.save(savepath)

# save database
def saveDataDB(datalist, dbpath):
    init_db(dbpath)
    conn = sqlite3.connect(dbpath)
    cur = conn.cursor()

    for data in datalist:
        for index in range(len(data)):
            if index == 4 or index == 5:
                continue
            data[index] = '"'+data[index]+'"'
        sql = 'insert into movie (info_link, pic_link,cname, ename, score, rated, inst, info) values(%s)'%",".join(data)
        cur.execute(sql)
        conn.commit()
    conn.close()


# 创建数据库
def init_db(dbpath):
    sql = '''
        create table movie 
        (
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            inst text,
            info text
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

# main
if __name__ == "__main__":
    # init_db('movie.db')
    main()