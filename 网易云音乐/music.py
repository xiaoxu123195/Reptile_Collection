# url = 'https://music.163.com/#/discover/toplist?id=19723756'

import requests
import re

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}

url = 'https://music.163.com/discover/toplist?id=19723756'

response = requests.get(url=url, headers=headers)
html_data = response.text
# print(html_data)
music_info = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>', html_data)

for info in music_info:
    music_url = f'http://music.163.com/song/media/outer/url?id={info[0]}'
    print(info[1], music_url)
    # 清除一些特殊符号，避免导致报错
    title = info[1]
    title = re.sub('[\\/:*?"<>|]', '', title)
    # .content 获取二进制数据
    music_data = requests.get(music_url).content
    with open(f'music/{title}.mp3', mode='wb') as f:
        f.write(music_data)


