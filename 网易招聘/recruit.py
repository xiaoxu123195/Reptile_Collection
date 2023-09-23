import requests
import json
import pprint
import csv
import time

f = open('job.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '职位名称',
    '工作地点',
    '工作部门',
    '工作性质',
    '需求人数',
    '要求学历',
    '职位描述',
    '职务要求',
])
csv_writer.writeheader()

url = 'https://hr.163.com/api/hr163/position/queryPage'

headers = {
    'referer': 'https://hr.163.com/job-list.html',
    'content-type': 'application/json;charset=UTF-8',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
}

for j in range(1, 11):

    data = {
        'currentPage': 1,
        'pageSize': 10,
    }

    res = requests.post(url=url, headers=headers, data=json.dumps(data))
    # print(res.text)
    json_data = json.loads(res.text)
    # pprint.pprint(json_data)
    for i in range(0, 10):
        job_name = json_data['data']['list'][i]['name']  # 职位名称
        description = json_data['data']['list'][i]['description']  # 职位描述
        description = description.replace('\n', '')
        workPlaceNameList = json_data['data']['list'][i]['workPlaceNameList'][0]  # 工作地点
        firstDepName = json_data['data']['list'][i]['firstDepName']  # 工作部门
        firstPostTypeName = json_data['data']['list'][i]['firstPostTypeName']  # 工作性质
        recruitNum = json_data['data']['list'][i]['recruitNum']  # 需求人数
        reqEducationName = json_data['data']['list'][i]['reqEducationName']  # 要求学历
        if reqEducationName == 'null':
            reqEducationName = '学历不限'
        requirement = json_data['data']['list'][i]['requirement']  # 职务要求
        requirement = requirement.replace('\n', '')
        dit = {
            '职位名称': job_name,
            '工作地点': workPlaceNameList,
            '工作部门': firstDepName,
            '工作性质': firstPostTypeName,
            '需求人数': recruitNum,
            '要求学历': reqEducationName,
            '职位描述': description,
            '职务要求': requirement,
        }
        csv_writer.writerow(dit)
        # print(job_name, workPlaceNameList, firstDepName, firstPostTypeName, recruitNum, reqEducationName, description,
        # requirement)
        # time.sleep(0.5)
