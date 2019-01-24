# https://www.cnblogs.com/shapeL/p/9051856.html

import requests
import urllib3
import json

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
payload = {'txtUserName': 'chn0622@sina.com', 'txtPassword': 'chn432431'}
url = 'https://www.shwzoo.com/tools/submit_ajax.ashx?action=user_login'

response = requests.post(url, payload, verify=False)

print(response.status_code)

# dict类型
print(response.json())
print(type(response.json()))

# ************** json ********************************************
# https://www.cnblogs.com/shapeL/p/9037670.html
# Serialize ``obj`` to a JSON formatted ``str``
# str类型
print(json.dumps(response.json(), ensure_ascii=False, sort_keys=True, indent=4))
# Serialize ``obj`` as a JSON formatted stream to ``fp`` (a``.write()``-supporting file-like object).
# json.dump()

print(response)
print(type(response))


# ***************** dict 接口测试中的常用操作 *************************************
# dict = response.json()
# # 获取第一层字典中的数据
# # 若dict中没有'msg'，报错KeyError
# print(dict['msg'])
# # 若dict中没有'code'，返回none
# print(dict.get('code'))
# print(dict.keys())
# print(dict.values())
# # 遍历key
# for key in dict.keys():
#     print(key)
# # 遍历value
# for value in dict.values():
#     print(value)
# # 遍历整个字典
# for key in dict:
#     print(key + ':' + str(dict[key]))
# ************************dict 常用操作****************************************
# dict = {'code': '200', 'message': '', 'redirect': '', 'value': {'name': '嗯嗯', 'title': '36', 'value': '123'}}
# # 获取第一层
# print(dict['value'])
# # 获取第二层
# print(dict['value']['name'])
# # 遍历字典项
# for item in dict.items():
#     print(item)
# # 删除'code'键值对
# del dict['code']
# print(dict)
# # 清空字典
# dict.clear()
# print(dict)
# # 删除字典
# del dict
# *****************************************************************************