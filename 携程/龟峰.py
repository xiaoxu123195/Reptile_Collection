import requests
import json
import time
import csv
import re

c = open(r'guifeng.csv', 'a+', newline='', encoding='utf-8')
fieldnames = ['user', 'time', 'score', 'content']
writer = csv.DictWriter(c, fieldnames=fieldnames)
writer.writeheader()

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}

postUrl = "https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList"

data_1 = {
    "pageid": "290510",
    "viewid": "127481",
    "tagid": "-11",
    "pagenum": "1",
    "pagesize": "10",
    "contentType": "json",
    "SortType": "1",
    "head": {
        "appid": "100013776",
        "cid": "09031010311083118856",
        "ctok": "",
        "cver": "1.0",
        "lang": "01",
        "sid": "8888",
        "syscode": "09",
        "auth": "",
        "extension": [
            {
                "name": "protocal",
                "value": "https"
            }
        ]
    },
    "ver": "7.10.3.0319180000"
}

html = requests.post(postUrl, data=json.dumps(data_1)).text
html = json.loads(html)
jingqu = '龟峰'
pages = html['data']['totalpage']
datas = []
for j in range(pages):
    data1 = {
        "pageid": "290510",
        "viewid": "127481",
        "tagid": "-11",
        "pagenum": str(j + 1),
        "pagesize": "10",
        "contentType": "json",
        "SortType": "1",
        "head": {
            "appid": "100013776",
            "cid": "09031010311083118856",
            "ctok": "",
            "cver": "1.0",
            "lang": "01",
            "sid": "8888",
            "syscode": "09",
            "auth": "",
            "extension": [
                {
                    "name": "protocal",
                    "value": "https"
                }
            ]
        },
        "ver": "7.10.3.0319180000"
    }
    datas.append(data1)

for k in datas[:50]:
    print('正在抓取第' + k['pagenum'] + "页")
    time.sleep(3)
    html1 = requests.post(postUrl, data=json.dumps(k)).text
    html1 = json.loads(html1)
    comments = html1['data']['comments']

    for i in comments:
        user = i['uid']
        time1 = i['date']
        score = i['score']
        content = i['content']
        content = re.sub(" ", "", content)
        content = re.sub("", "", content)

        writer.writerow({'user': user, 'time': time1, 'score': score, 'content': content})
c.close()
