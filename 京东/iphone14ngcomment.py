import requests


url = "https://club.jd.com/comment/productPageComments.action"

for j in range(0, 11):
    data = {
        'productId': '100038004389',
        'score': '1',
        'sortType': '5',
        'page': f'{j}',
        'pageSize': '10',
        'isShadowSku': '0',
        'fold': '1',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36',
    }

    response = requests.get(url=url, params=data, headers=headers).json()
    for i in response['comments']:
        content = i['content']
        creationTime = i['creationTime']
        score = i['score']
        productColor = i['productColor']
        productSize = i['productSize']
        # print(content, creationTime, score, productColor, productSize)
        with open('pachong012.txt', mode='a', encoding='utf-8') as f:
            f.write(content+creationTime+str(score)+productColor+productSize)
            f.write('\n')
