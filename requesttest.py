import requests
import json
import codecs
import re
# r = requests.get("http://api.douban.com/v2/movie/top250", stream=True)
# # r = requests.get("https://www.baidu.com", verify=False)
#
# # payload = {"txtUserName": "chn0622@sina.com", "txtPassword": "chn432431"}
# # r = requests.post("http://www.shwzoo.com/login.aspx", payload)
#
# print(type(r))
# print(r.status_code)
# print(r.raise_for_status())
# # unicode 乱码
# print(type(r.text))
# print(r.text)
# # byte
# print(type(r.content))
# print(r.content)
# print(r.content.decode("utf-8"))
# # 与r.content.decode("utf-8")效果一致，避免乱码产生
# print(r.encoding)
# r.encoding = "utf-8"
# print(r.text)
#
# # request.response.json() 实际上是执行了json.loads()方法
# print(r.json())
# print(type(r.json()))
# print(json.loads(r.text))
# # print(r.raw)
# # print(r.raise_for_status())



# # session对象
# s = requests.session()
# s.get("http://httpbin.org/cookies/set/sessioncookie/123456789")
# r = s.get("http://httpbin.org/cookies")
# print(r.text)

# r = requests.get("https://www.baidu.com", verify=False)
# print(r.status_code)
# r.json()

# r = requests.get('https://api.github.com/requests/kennethreitz/requests/issues/482')
# print(r.status_code)

# url = "https://www.zhihu.com"
# headers = {
#     "User-Agent":
#     "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"
# }
# r = requests.get(url, headers=headers)
# print(r.text)
# print(r.encoding)

# 压制警告：InsecureRequestWarning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
url = "https://www.12306.cn"
# url = "https://www.baidu.com"
r = requests.get(url, verify=False)
print(type(r.status_code), r.status_code)
print(type(r.headers), r.headers)
print(type(r.cookies), r.cookies.items())
print(type(r.url), r.url)
print(type(r.history), r.history)

for key, value in r.cookies.items():
    print(key+"="+value)
