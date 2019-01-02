import xml.etree.ElementTree as ElementTree
import os.path

proDir = os.path.split(os.path.realpath(__file__))[0]
sqlPath = os.path.join(proDir, "testFile", "sql.xml")

tree = ElementTree.parse(sqlPath)
root = tree.getroot()
print(root)

# 遍历root的子元素
for child in root:
    child_name = child.get("name")
    print(child_name)

# ***************** 修改interfaceTest-common.py中的xml部分
# 三层嵌套dict
database = {}
# 遍历tree的子元素：第二层
for db in tree.findall("database"):
    db_name = db.get("name")
    print(db_name)
    table = {}
    # 遍历db的子元素，即tree的孙元素：第三层
    for tb in db:
        tb_name = tb.get("name")
        print(tb_name)
        sql = {}
        # 遍历tb的子元素，即db的孙元素：第四层
        for data in tb:
            sql_author = data.get("author")
            print(sql_author)
            # dict类型的数据写入attrib和value 底层dict
            sql[sql_author] = data.text
        # dict类型的数据写入dict 中层dict
        table[tb_name] = sql
    # dict类型写入dict 最外层dict
    database[db_name] = table
print(database)

# 从嵌套的dict中取出最底层的dict dict取出属性对应的值的方法是get
database_dict = database.get("test").get("book")
print(database_dict)
# 从最底层的dict取出Harry属性对应的值 dict取出属性对应的值的方法是get
sql = database_dict.get("Harry")
print(sql)

