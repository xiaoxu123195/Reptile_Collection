import requests
from lxml import etree
import csv

f = open('pring.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '排名',
    '学校名称',
    '省市',
])
csv_writer.writeheader()

url = 'https://www.dxsbb.com/news/44368.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'content-type': 'text/html',
}
response = requests.get(url, headers=headers)
response.encoding = response.apparent_encoding
html_data = response.text
tree = etree.HTML(html_data)
ranking = tree.xpath('//*[@id="content"]/div[2]/div/table//tr/td[1]/text()')
for i in ranking:
    rank = i
school_name = tree.xpath('//*[@id="content"]/div[2]/div/table//tr/td[2]/text()')
for j in school_name:
    name = j
locals = tree.xpath('//*[@id="content"]/div[2]/div/table//tr/td[3]/text()')
for k in locals:
    local = k

