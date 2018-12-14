import re

content = "Extra things hello 123455 World_this is a regex Demo extra things"

# \d+ 替换内容
# content = re.sub('\d+', '', content)
# print(content)

# r代表后面字符串为普通字符串，为了防止转义
# \1是获取第一个匹配的结果
# （\d+）添加内容
content = re.sub('(\d+)', r'\1 7890', content)
print(content)
