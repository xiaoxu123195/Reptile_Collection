import pprint
import requests
import re
import json
from lxml import etree

url = 'https://www.acfun.cn/u/29946310'
headers = {
    'Referer': 'https://www.acfun.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36 '
}
response = requests.get(url=url, headers=headers)
tree = etree.HTML(response.text)
# response = requests.get(url=url, headers=headers).text
# print(response)
# json_data = json.loads(html_data)
# pprint.pprint(response)
# tree = ''.join(tree)
lis = tree.xpath('//*[@id="ac-space-video-list"]//a/@href')
# print(lis)
for li in lis:
    print(li)
