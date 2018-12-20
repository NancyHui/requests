import pymysql

# 连接数据库方法一
# 在变量前加*，则参数会作为一个元组存在args中
# 在变量前加**，则参数会作为字典存在args中
data = {
    'host': 'localhost',
    'user': 'root',
    'password': '123456',
    'port': 3306,
    'db': 'test'
}
# 打开数据库连接
db = pymysql.connect(**data)

# # 连接数据库方法二
# db = pymysql.connect(host="127.0.0.1", user="root", password="123456", port=3306, db="test")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 增、删、改
# 增加方式一
# sql1 = 'insert into book(bookname, price, author) values("python", 46.6, "Harry") '
# 增加方式二：格式化 <注意>：values中使用"%s" (使用双引号是因为sql字符串使用的是单引号，否则会出现错误)
bookname = "python"
price = 46
author = "Harry"
sql1 = 'insert into book(bookname, price, author) values("%s", %d, "%s") ' % (bookname, price, author)

try:
    # 执行sql语句
    cursor.execute(sql1)
    # 提交到数据库执行
    db.commit()
except:
    # 如果发生错误则回滚
    db.rollback()

# 查询
sql2 = "select * from book"

try:
    cursor.execute(sql2)
    results = cursor.fetchall()
    # results为tuple类型 ((1, 'java', 60, 'kevin'), (2, 'c', 50, 'marry'), (12, 'python', 46, 'Harry'))
    print(results)
    for row in results:
        id = row[0]
        bookname = row[1]
        price = row[2]
        author = row[3]
        print("id=%d, bookname=%s, price=%f, author=%s" % (id, bookname, price, author))
        # print(id, bookname, price, author)

    #  第一行（row）,执行多次则是下一个行
    result = cursor.fetchone()
    print(result)
except :
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
