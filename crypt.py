# https://www.jianshu.com/p/bdadf8607a3b
# https://www.jianshu.com/p/add7518a3fbe
# **************************** MD5加密 ****************************************************
import hashlib


def md5(string):
    """

    :param string:
    :return:
    """
    m = hashlib.md5()
    # update()输入应为bytes类型，需用.encode('utf-8')将str转为bytes型
    m.update(string.encode('utf-8'))
    # # the bytes
    # return m.digest()
    # # a unicode object of double length
    return m.hexdigest()


print(md5('ssfan'))


# ******************************* ASE加密--1 *******************************************************
from Crypto.Cipher import AES
# 加密 AES加密里面有两个关键，一个是key（必须为16,24,32位），一个是VI（必须为16位）
obj = AES.new('This is a key123'.encode('utf-8'), AES.MODE_CBC, 'This is an IV456'.encode('utf-8'))
# AES.MODE_CBC message必须为16位
message = "The answer is no".encode('utf-8')
ciphertext = obj.encrypt(message)
print(ciphertext)
# 解密 解密者必须要同时知道key和VI才可以解密
obj2 = AES.new('This is a key123'.encode('utf-8'), AES.MODE_CBC, 'This is an IV456'.encode('utf-8'))
print(obj2.decrypt(ciphertext))

# ******************************* ASE加密--2 *******************************************************
import base64
from Crypto.Cipher import AES


# AES加密
def aes_crypt(key, iv, passwd):
    """
    AES加密算法（key，iv，passwd输入均应为bytes类型，选择MODE_CBC类型加密）
    :param key: 秘钥（定值，16位长度）
    :param iv: 偏移（定值，16位长度）
    :param passwd: 密码
    :return: 返回值再经过base64加密后
    """
    BS = AES.block_size  # 获取AES数据位数（16位）
    # 补位，补够16位   匿名函数
    pad = (lambda s: s + (BS - len(s) % BS) * '#')
    print(pad(passwd))
    aes = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    return base64.b64encode(aes.encrypt(pad(passwd).encode('utf-8')))


aes_key = 'QWHeJfoWQgaYasdf'
aes_iv = '1111111111222345'
password = '123456'
# 注意，经过aes_crypt加密的密文是bytes类型
password = aes_crypt(aes_key, aes_iv, password).decode('utf-8')
print(password)

# 安装AES库
# 第一步，安装crypto
# pip install crypto
# 第二步，安装pycryptodome
# pip install pycryptodome
# 第三步，改文件夹名称
# 进入Python3的目录下的\lib\site-packages，将crypto文件夹更名为Crypto（注意是大写的C，否则导入模块失败）