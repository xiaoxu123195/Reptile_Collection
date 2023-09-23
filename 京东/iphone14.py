import requests
import csv

f = open('iphone14.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    'content',
    'creationTime',
    'score',
    'productColor',
    'productSize',
])
csv_writer.writeheader()

url = "https://club.jd.com/comment/productPageComments.action"

for j in range(0, 11):
    data = {
        # 'callback': 'fetchJSON_comment98',
        'productId': '100038004389',
        'score': '0',
        'sortType': '5',
        'page': f'{j}',
        'pageSize': '10',
        'isShadowSku': '0',
        'rid': '0',
        'fold': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    response = requests.get(url=url, params=data, headers=headers).json()
    # print(response)
    for i in response['comments']:
        content = i['content']
        creationTime = i['creationTime']
        score = i['score']
        productColor = i['productColor']
        productSize = i['productSize']

        dit = {
            'content': content,
            'creationTime': creationTime,
            'score': score,
            'productColor': productColor,
            'productSize': productSize,
        }
        csv_writer.writerow(dit)
        # print(content, creationTime, score, productColor, productSize)









