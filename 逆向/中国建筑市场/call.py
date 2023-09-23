import requests
import execjs

for i in range(0, 2):
    url = f'http://jzsc.mohurd.gov.cn/api/webApi/dataservice/query/comp/list?pg={i}&pgsz=15&total=450'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'Referer': 'http://jzsc.mohurd.gov.cn/data/company'
    }
    response = requests.get(url, headers=headers).text
    # print(response)

    with open('./建筑市场AES.js', 'r', encoding='utf-8') as f:
        jscode = f.read()

    # s是要执行的函数 data是加密的数据
    ctx = execjs.compile(jscode).call('h', response)
    print(ctx)
