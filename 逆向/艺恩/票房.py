import pprint

import execjs
import requests

url = 'https://www.endata.com.cn/API/GetData.ashx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
for i in range(2021, 2023):
    data = {
        'year': i,
        'MethodName': 'BoxOffice_GetYearInfoData',
    }

    response = requests.post(url, headers=headers, data=data).text
    # print(response)

    with open('./123.js', 'r', encoding='utf-8') as f:
        jscode = f.read()

    # s是要执行的函数 data是加密的数据
    ctx = execjs.compile(jscode).call('webInstace.shell', response)
    print(ctx)
