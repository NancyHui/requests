# https://my.oschina.net/u/3041656/blog/793467
import configparser
import time
import os
# 实例化ConfigParser对象
cf = configparser.ConfigParser()
print(type(cf))

proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

# ------------os.path-------------------------------
# print(__file__)
# print(type(__file__))
# # realpath = abspath
# print(os.path.realpath(__file__))
# print(os.path.abspath(__file__))
#
# print(os.path.dirname(os.path.realpath(__file__)))
# print(os.path.basename(os.path.realpath(__file__)))
# print(os.path.split(os.path.realpath(__file__)))
# print((os.path.split(os.path.realpath(__file__)))[0])
# print((os.path.split(os.path.realpath(__file__)))[1])
#
# print(os.path.join(*(os.path.split(os.path.realpath(__file__)))))
#
# proDir = os.path.split(os.path.realpath(__file__))[0]
# print("proDir", proDir)
# configPath = os.path.join(proDir, "config.ini")
# print("configPath", configPath)
# ------------os.path-------------------------------

# ****************************读取********************************
# read()中的filename指的是路径
# cf.read('D:\pycharmwork\\test\config.ini')
cf.read(configPath)

print(cf.sections())
# list 得到所有的section
# ['DATABASE', 'HTTP', 'EMAIL']
print(type(cf.sections()))

# section对应的option
# ['host', 'username', 'password', 'port', 'database']
print(cf.options(cf.sections()[0]))

# section对应的键值对(option: value)
# [('host', '127.0.0.1'), ('username', 'root'), ('password', '123456'), ('port', '3306'), ('database', 'book')]
print(cf.items(cf.sections()[0]))

# 得到section中option的值，返回为string类型
section = cf.sections()[0]
option = cf.options(section)[0]
print(cf.get(section, option))
print(cf.get('DATABASE', 'host'))


def getDATABASEValue(self, name):
    value = self.cf.get("DATABASE", name)
    return value
#
# ****************************读取********************************


# ****************************写入********************************
# cf.write('D:\pycharmwork\\test\config.ini') 这是错误的，在cf.write()中需要传入的是fp，即打开的文件
cf.add_section("ADD")
# # the value of option must be String
cf.set("ADD", "Time", "20181219")

# ------------file-------------------------------
# http://www.runoob.com/python/file-methods.html
# https://www.cnblogs.com/bearkchan/p/8046494.html
# w 覆盖原内容
# a 末尾追加内容
# fp--file对象，使用open创建
cf.write(open('D:\pycharmwork\\test\config.ini', 'a'))
# ------------file-------------------------------

# ------------time-------------------------------
# # time.time()--second
# # time.localtime(time.time())--a time tuple
# # time.asctime(time.localtime(time.time()))--string
# # 格式化成2016-03-20 11:45:39形式
# # print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# # 格式化成Sat Mar 28 22:24:24 2016形式
# # print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
# ------------time-------------------------------

cf.set("ADD", "Time", time.asctime(time.localtime(time.time())))
cf.read(r'D:\pycharmwork\test\config.ini')
print(cf.sections())
print(cf.items(cf.sections()[0]))

def setConfigValue(self, name, value):
    cfg = self.cf.set("config", name, value)
    fp = open(r'config.ini', 'w')
    cfg.write(fp)


# 基本的读取操作：
#
# -read(filename)               直接读取文件内容
# -sections()                      得到所有的section，并以列表的形式返回
# -options(section)            得到该section的所有option
# -items(section)                得到该section的所有键值对
# -get(section,option)        得到section中option的值，返回为string类型
# -getint(section,option)    得到section中option的值，返回为int类型，还有相应的getboolean()和getfloat() 函数。

# 基本的写入操作：
#
# -write(fp)  将config对象写入至某个 .init 格式的文件  Write an .ini-format representation of the configuration state.
# -add_section(section)   添加一个新的section
# -set( section, option, value   对section中的option进行设置，需要调用write将内容写入配置文件
# -remove_section(section)  删除某个 section
# -remove_option(section, option)