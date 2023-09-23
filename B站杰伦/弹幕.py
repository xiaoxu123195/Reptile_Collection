import requests
import re


url = 'https://api.bilibili.com/x/v1/dm/list.so?oid=765060141'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
}
response = requests.get(url=url, headers=headers)
# 解决网页数据乱码
response.encoding = 'utf-8'
content_list = re.findall('<d p=".*?">(.*?)</d>', response.text)
print(content_list)
for content in content_list:
    with open('弹幕.txt', mode='a', encoding='utf-8') as f:
        f.write(content)
        # 把数据换行
        f.write('\n')
