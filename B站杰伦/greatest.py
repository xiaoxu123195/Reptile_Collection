import requests
import re
import json
import pprint
# 音视频合成模块
import subprocess

url = 'https://www.bilibili.com/video/BV1ua411p7iA?spm_id_from=333.337.search-card.all.click'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36',
    'referer': 'https://search.bilibili.com/all?keyword=%E6%9C%80%E4%BC%9F%E5%A4%A7%E7%9A%84%E4%BD%9C%E5%93%81'
               '&from_source=webtop_search&spm_id_from=333.1007 ',
}

response = requests.get(url=url, headers=headers)
# print(response.text)
title = re.findall('"title":"(.*?)","pubdate"', response.text)[0].replace(' ', '')
title = re.sub(r'[\/:*?"<>|]', '', title)
# title = title.replace('|', '')  # 也可以
html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]  # 取出来的为json字符串
json_data = json.loads(html_data)
# pprint.pprint(json_data)
audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
video_url = json_data['data']['dash']['video'][0]['baseUrl']
print(audio_url)
print(video_url)
print(title)
# # 获取音频的二进制数据
# audio_content = requests.get(url=audio_url, headers=headers).content
# # 获取视频的二进制数据
# video_content = requests.get(url=video_url, headers=headers).content
# with open('video\\' + title + '.mp3', mode='wb') as a:
#     a.write(audio_content)
# with open('video\\' + title + '.mp4', mode='wb') as v:
#     v.write(video_content)
# 通过ffmpeg这个软件命令 进行视频合成
cmd = f"ffmpeg -i video\\{title}.mp4 -i video\\{title}.mp3 -c:v copy -c:a aac -strict experimental video\\{title}output.mp4"
subprocess.run(cmd, shell=True)
