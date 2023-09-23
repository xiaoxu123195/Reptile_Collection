import pprint
import requests
import re
import json
from lxml import etree
# 爬取一整页全部数据
link = 'https://www.acfun.cn/u/29946310'
headers = {
    'Referer': 'https://www.acfun.cn/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36 '
}
response = requests.get(url=link, headers=headers)
tree = etree.HTML(response.text)

lis = tree.xpath('//*[@id="ac-space-video-list"]//a/@href')
for li in lis:
    # print(li)
    url = f'https://www.acfun.cn{li}'
    print(url)
    headers = {
        'Referer': f'https://www.acfun.cn{li}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                      'Safari/537.36 '
    }

    response = requests.get(url=url, headers=headers)
    title = re.findall('<title >(.*?) - AcFun弹幕视频网 - 认真你就输啦 \(\?ω\?\)\ノ\- \( ゜- ゜\)つロ</title>', response.text)[0]
    html_data = re.findall('window.pageInfo = window.videoInfo =(.*?);', response.text)[0]
    # html_data = ''.join(html_data)

    # print(type(html_data))
    json_data = json.loads(html_data)
    # pprint.pprint(json_data)
    m3u8_url = \
        json.loads(json_data['currentVideoInfo']['ksPlayJson'])['adaptationSet'][0]['representation'][0]['backupUrl'][0]
    # pprint.pprint(m3u8_url)
    # print(m3u8_url)
    m3u8_data = requests.get(url=m3u8_url, headers=headers).text
    # print(m3u8_data)
    m3u8_data = re.sub('#E.*', '', m3u8_data).split()  # split()把数据封装成列表
    # print(m3u8_data)
    for ts in m3u8_data:
        ts_name = ts.split('.')[1]  # 字符串分割
        ts_url = 'https://ali-safety-video.acfun.cn/mediacloud/acfun/acfun_video/' + ts
        ts_content = requests.get(url=ts_url, headers=headers).content
        with open('video\\' + '王春蒙' + title + '.mp4', mode='ab') as f:
            f.write(ts_content)
            # print(ts_url)
