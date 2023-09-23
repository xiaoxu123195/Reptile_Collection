import requests
import re
import json
import csv

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

with open('data.csv', mode='a', newline='', encoding='utf-8') as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(['area', 'curConfirm', 'curConfirmRelative', 'confirmed', 'crued', 'died'])

url = 'https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner'

# post 一般需要带有请求体
response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)

json_str = re.findall('"component":\[(.*)\],', html_data)[0]
json_data = json.loads(json_str)
caseList = json_data['caseList']
for case in caseList:
    area = case['area']  # 省份
    curConfirm = case['curConfirm']  # 确诊人数
    curConfirmRelative = case['curConfirmRelative']
    confirmed = case['confirmed']  # 累计确诊
    crued = case['crued']  # 治愈人数
    died = case['died']  # 死亡人数
    print(area, curConfirm, curConfirmRelative, confirmed, crued, died)

    with open('data.csv', mode='a', newline='', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow([area, curConfirm, curConfirmRelative, confirmed, crued, died])


