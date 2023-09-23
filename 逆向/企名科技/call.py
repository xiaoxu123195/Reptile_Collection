import pprint

import execjs
import requests

url = 'https://vipapi.qimingpian.cn/DataList/productListVip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
data1 = {
    'time_interval': '',
    'tag': '',
    'tag_type': '',
    'province': '',
    'lunci': '',
    'page': 1,
    'num': 20,
    'unionid': '',
}

response = requests.post(url, headers=headers, data=data1).json()
data = (response['encrypt_data'])

with open('./123.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

# s是要执行的函数 data是加密的数据
ctx = execjs.compile(jscode).call('s', data)
# print(ctx)
# pprint.pprint(ctx)
data_list = ctx['list']
for lists in data_list:
    # print(lists)
    pprint.pprint(lists)


