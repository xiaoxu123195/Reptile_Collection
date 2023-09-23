# PyV8只支持python3.3 所以不建议使用

import PyV8
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

with PyV8.JSContext() as ctx:
    ctx.eval(jscode)
    ctx_data = ctx.locals.add(data)
    print(ctx_data)

