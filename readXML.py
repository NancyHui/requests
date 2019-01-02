# https://my.oschina.net/u/3041656/blog/820023
import xml.etree.ElementTree as ElementTree
import os.path

proDir = os.path.split(os.path.realpath(__file__))[0]
sqlPath = os.path.join(proDir, "testFile", "sql.xml")

# 1. ElementTree represents the whole XML document as a tree 节点树
# 2. Element represents a single node in this tree 节点

# Parse XML document into element tree
tree = ElementTree.parse(sqlPath)

# ************************ Element ***************************
# Return root element of this tree
root = tree.getroot()
print(root)
# 节点的标签名称和属性
print(root.tag, ":", root.attrib)
# root-datebase-table-sql
print(root[0][0][0].text)
print('******************************')

# # Parse XML document from sequence of string fragments
element = ElementTree.fromstringlist(r'<sql author="Harry"> SELECT * FROM book WHERE author = %s</sql>')
print(element)
print(element.tag, ":", element.attrib)
print(element.text)

# 遍历xml文件第二层
for child in root:
    # 第二层节点的标签名称和属性
    print(child.tag, ":", child.attrib)
    # 遍历xml文件第三层
    for children in child:
        # 第三层节点的标签名称和属性
        print(children.tag, ":", children.attrib)
print("***************************************************")
# ********************** ElementTree ************************
# Find all matching subelements by tag name or path
# Return list containing all matching elements in document order
# findall只找到下一级
for db in tree.findall("database"):
    db_name = db.get("name")
    print(db_name)

# iter迭代寻找（分层）
for db in tree.iter("table"):
    db_name = db.get("name")
    print(db_name)

# **************************** Element *****************************
# Element
# class xml.etree.ElementTree.Element(tag, attrib={}, **extra)
#
# 　　tag：string，元素代表的数据种类。
# 　　text：string，元素的内容。
# 　　tail：string，元素的尾形。
# 　　attrib：dictionary，元素的属性字典。
# 　　
# 　　＃针对属性的操作
# 　　clear()：清空元素的后代、属性、text和tail也设置为None。
# 　　get(key, default=None)：获取key对应的属性值，如该属性不存在则返回default值。
#     Get element attribute.Returns a string containing the attribute value, or the default if attribute was not found.
# 　　items()：根据属性字典返回一个列表，列表元素为(key, value）。
# 　　keys()：返回包含所有元素属性键的列表。
# 　　set(key, value)：设置新的属性键与值。
#
# 　　＃针对后代的操作
# 　　append(subelement)：添加直系子元素。
# 　　extend(subelements)：增加一串元素对象作为子元素。＃python2.7新特性
# 　　find(match)：寻找第一个匹配子元素，匹配对象可以为tag或path。
# 　　findall(match)：寻找所有匹配子元素，匹配对象可以为tag或path。
# 　　findtext(match)：寻找第一个匹配子元素，返回其text值。匹配对象可以为tag或path。
# 　　insert(index, element)：在指定位置插入子元素。
# 　　iter(tag=None)：生成遍历当前元素所有后代或者给定tag的后代的迭代器。＃python2.7新特性 以当前元素为根节点 创建树迭代器
# 　　iterfind(match)：根据tag或path查找所有的后代。
# 　　itertext()：遍历所有后代并返回text值。
# 　　remove(subelement)：删除子元素。

# **************************** ElementTree ***************************************
# ElementTree
# class xml.etree.ElementTree.ElementTree(element=None, file=None)
# 　　element如果给定，则为新的ElementTree的根节点。
#
# 　　_setroot(element)：用给定的element替换当前的根节点。慎用。
# 　　
# 　　＃ 以下方法与Element类中同名方法近似，区别在于它们指定以根节点作为操作对象。
# 　　find(match)
# 　　findall(match)
# 　　findtext(match, default=None)
# 　　getroot()：获取根节点.
# 　　iter(tag=None)
# 　　iterfind(match)
# 　　parse(source, parser=None)：装载xml对象，source可以为文件名或文件类型对象.
# 　　write(file, encoding="us-ascii", xml_declaration=None, default_namespace=None,method="xml")　