# 实现爬取全部数据 拿到所有id
import requests
import re
import pprint
import json

link = 'https://www.acfun.cn/u/29946310'
for i in range(0, 3):
    data = {
        'quickViewId': 'ac-space-video-list',
        'reqID': f'{i}',
        'ajaxpipe': '1',
        'type': 'video',
        'order': 'newest',
        'page': f'{i+1}',
        'pageSize': '20',
    }
    print(data)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                      'Safari/537.36 '
    }
    response_data = requests.get(url=link, params=data, headers=headers).text
    # pprint.pprint(response)
    id_list = re.findall('atomid.*?":.*?"(\d+).*?",', response_data)
    for video_id in id_list:
        print(video_id)

