import re

html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君">但愿人长久</a>
        </li>
    </ul>
</div>'''

# result.groups() = (匹配第一个(.*?)的内容, 匹配第二个(.*?)的内容)  "str"
# result.groups(1) = 匹配第一个(.*?)的内容
# result.groups(2) = 匹配第二个(.*?)的内容
result = re.search('<li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(type(result))
print(type(result.group()))
print(result.groups())
print(result.group(1))
print(result.group(2))

# # type(results) = list
# # results = [(匹配第一个(.*?)的内容，匹配第二个(.*?)的内容，匹配第三个(.*?)的内容),(..,)...]
# results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(results)
# print(type(results))
# for result in results:
#     print(result)
#     print(result[0], result[1], result[2])

# # # results = [(匹配第一个(<a.*?>)的内容，匹配第二个(\w+)的内容，匹配第三个(</a>)的内容),(..,)...]
# results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
# print(results)
# for result in results:
#     print(result[1])
