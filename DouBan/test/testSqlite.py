import sqlite3
from sqlite3.dbapi2 import connect  

conn = sqlite3.connect('test.db')
# print("opened database successfully")

# 获取游标
c = conn.cursor()

# 创建表格
# sql = '''
#     create table company
#     (id int primary key not null,
#     name text not null,
#     age int not null,
#     address char(50),
#     salary real);
# '''
# 数据插入
# sql = '''
#     insert into company values (1, 'shuchenglin', 25, 'BeiJing', 10000);
# '''

sql = " select id, name from company"

cursor = c.execute(sql)
for i in cursor:
    print('id = ', i[0])
    print('name = ', i[1])
# 提交数据库操作
# conn.commit()
# 关闭数据库
conn.close()

print("查询完成")