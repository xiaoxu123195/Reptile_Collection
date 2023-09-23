import requests
import pymysql


class articleData:
    def __init__(self, content, creationTime, score, productColor, productSize):
        self.content = content
        self.creationTime = creationTime
        self.score = score
        self.productColor = productColor
        self.productSize = productSize


def saveData(DataObject):
    count = pymysql.connect(host='localhost', port=3306, user='root', password='', db='xiejiayi')
    db = count.cursor()
    sql = f"insert into pachong012(content,creationTime,score,productColor,productSize) " \
          f"values ('{DataObject.content}','{DataObject.creationTime}','{DataObject.score}','{DataObject.productColor}','{DataObject.productSize}')"
    db.execute(sql)
    count.commit()
    db.close()


def getWebData():
    url = "https://club.jd.com/comment/productPageComments.action"

    for j in range(0, 31):
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

            # 下面两行是调用方法往数据库里面写数据的，调试时可以注释掉
            # article_data = articleData(content, creationTime, score, productColor, productSize)
            # saveData(article_data)

            # 下面两行是写入txt文件的
            with open('测试.txt', mode='a', encoding='utf-8') as f:
                f.write(content)
                f.write('\n')


if __name__ == "__main__":
    getWebData()
