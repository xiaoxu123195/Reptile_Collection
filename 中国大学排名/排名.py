import requests
from lxml import etree
from urllib import request

url = 'https://www.shanghairanking.cn/rankings/bcur/202211'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'content-type': 'text/html',
}

response = requests.get(url, headers=headers)
# print(response.encoding)  # 查看网页返回的字符集类型
# print(response.apparent_encoding)  # 自动判断字符集类型
response.encoding = response.apparent_encoding
html_data = response.text
tree = etree.HTML(html_data)
school_data = tree.xpath('//*[@id="content-box"]/div[2]/table/tbody/tr')
for school in school_data:
    school_rank = school.xpath('./td[1]/div/text()')[0].replace('\n', '')
    school_rank = school_rank.replace(' ', '')
    school_name = school.xpath('./td[2]/div/div[2]/div[1]/div/div/a/text()')[0]

    print(school_rank, school_name)
    # print(request.urlopen(url).geturl())
