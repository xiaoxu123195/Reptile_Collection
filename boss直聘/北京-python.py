import requests
import pprint
import json
import csv
import time

f = open('python.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '职位',
    '地点',
    '薪资',
    '经历学历',
    '招聘经理',
    '招聘类型',
    '招聘公司',
    '公司福利',
    '公司简介',
])
csv_writer.writeheader()

for j in range(1, 11):
    url = 'https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=%E5%8C%97%E4%BA%ACpython&city=100010000' \
          f'&experience=&degree=&industry=&scale=&stage=&position=&salary=&multiBusinessDistrict=&page={j}&pageSize=30 '

    headers = {
        'Referer': 'https://www.zhipin.com/web/geek/job?query=%E5%8C%97%E4%BA%ACpython&city=100010000',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                      'Safari/537.36 ',
        'cookie': 'wd_guid=4939db9c-d326-402b-8a3f-82aecae209f4; historyState=state; _bl_uid=zCleh5sn2t5ehk77I9tn7d35a2a9; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1657004833,1657253595,1657273073,1657461049; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1657461051; __zp_stoken__=58b9ddEk9aFBdFXclVHNPDy5KbltIA2J%2FGngpL1h3PQYhVhJLJxk8CAsDP2NLMV4EKVAPdzUHQ2N2EWQVL1ouCHRkW2o%2FBiQPCQRcIF1RTHMvGXwNO1JFFXAIbTR9f00ZIhNlR1VCWSYKAmVMGBZkQQIJEkdUVQNpMkg9IjMYCXtMAm0NWDYbDmx8GH8%2FRn9nOGdnZGkGJQ%3D%3D; __c=1657461049; __l=l=%2Fwww.zhipin.com%2Fweb%2Fgeek%2Fjob%3Fquery%3D%25E5%258C%2597%25E4%25BA%25ACpython%26city%3D100010000&r=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DGQsm3zZTEcoYthIrMx4DLHI9D4mTc2YJdh26rPmOyGumzO84YPhDxU2StFCH9AJW%26wd%3D%26eqid%3De4fa83dc0000cad50000000262cad937&g=&s=3&friend_source=0&s=3&friend_source=0; __a=41916942.1655789213.1657273073.1657461049.99.16.3.99'
        }

    response = requests.get(url=url, headers=headers)
    res = response.text
    json_data = json.loads(res)
    json_str = json.dumps(json_data)
    data2 = json.loads(json_str)
    for i in range(0, 29):
        jobName = data2['zpData']['jobList'][i]['jobName']  # 职位
        name = data2['zpData']['jobList'][i]['bossName']
        title = data2['zpData']['jobList'][i]['bossTitle']
        src = name + title  # 招聘经理
        city = data2['zpData']['jobList'][i]['cityName']
        city1 = data2['zpData']['jobList'][i]['areaDistrict']
        city2 = data2['zpData']['jobList'][i]['businessDistrict']
        local = city + city1 + city2  # 地点
        jobLabels = data2['zpData']['jobList'][i]['jobLabels']  # 经历学历
        jobLabel = ''.join(jobLabels)
        salaryDesc = data2['zpData']['jobList'][i]['salaryDesc']  # 薪资
        skills = data2['zpData']['jobList'][i]['skills']  # 类型
        skill = ''.join(skills)
        brandName = data2['zpData']['jobList'][i]['brandName']  # 招聘公司
        welfareList = data2['zpData']['jobList'][i]['welfareList']  # 招聘公司简介
        welfareLists = ''.join(welfareList)
        brandIndustry = data2['zpData']['jobList'][i]['brandIndustry']
        brandStageName = data2['zpData']['jobList'][i]['brandStageName']
        brandScaleName = data2['zpData']['jobList'][i]['brandScaleName']
        brief = brandIndustry + brandStageName + brandScaleName
        dit = {
            '职位': jobName,
            '地点': local,
            '薪资': salaryDesc,
            '经历学历': jobLabel,
            '招聘经理': src,
            '招聘类型': skill,
            '招聘公司': brandName,
            '公司福利': brief,
            '公司简介': welfareLists,
        }
        csv_writer.writerow(dit)
        # print(jobName, local, salaryDesc, jobLabel, src, skill, brandName, brief, welfareLists)
        time.sleep(1)  # 1秒好慢 就这样cookie都会失效
# pprint.pprint(json_data)
# zp_data = json.loads(json_data['zpData']['jobList'])[0]
# print(zp_data)
