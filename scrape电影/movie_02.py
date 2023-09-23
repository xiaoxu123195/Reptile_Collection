import requests
from lxml import etree
import csv

f = open('movie.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '名称',
    '时间',
    '详情',
    '导演',
])
csv_writer.writeheader()

for i in range(1, 11):
    url = f'https://ssr1.scrape.center/page/{i}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    new_url = 'https://ssr1.scrape.center'
    response = requests.get(url, headers).text
    tree = etree.HTML(response)
    data_details = tree.xpath('//*[@id="index"]/div[1]/div[1]/div')
    for data in data_details:
        detail_urls = data.xpath('./div/div/div[2]/a/@href')[0]
        time = data.xpath('./div/div/div[2]/div[2]/span[3]/text()')[0]
        detail_url = new_url + detail_urls
        new_response = requests.get(detail_url, headers=headers).text
        news = etree.HTML(new_response)
        name = news.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/a/h2/text()')[0]
        brief = news.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[4]/p/text()')[0]
        # .lstrip()表示删除文字左侧空格
        # .rstrip()表示删除字符串末尾的空格
        brief = brief.replace('\n', '').lstrip()
        director = news.xpath('//*[@id="detail"]/div[2]/div/div/div/div/div/p/text()')[0]
        dit = {
            '名称': name,
            '时间': time,
            '详情': brief,
            '导演': director,
        }
        csv_writer.writerow(dit)
