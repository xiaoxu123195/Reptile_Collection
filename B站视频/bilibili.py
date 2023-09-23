import json
import pprint
import requests
import re


def get_response(html_url):
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
    }
    response = requests.get(url=html_url, headers=headers)
    return response


def get_video_info(play_url):
    response = get_response(html_url=play_url)
    # print(response.text)
    title = re.findall('"title":"(.*?)","pubdate"', response.text)[0]  # 标题
    title = re.sub(r'[/\:*?"<>|]', '', title)
    html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]  # 视频信息
    # print(title)
    # print(html_data)
    json_data = json.loads(html_data)
    # pprint.pprint(json_data)  # 格式化展开效果
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    # print(title)
    # print(audio_url)
    # print(video_url)
    video_info = [title, audio_url, video_url]
    return video_info


def save(title, audio_url, video_url):
    audio_content = get_response(html_url=audio_url).content
    video_content = get_response(html_url=video_url).content
    with open('video\\' + title + '.mp3', mode='wb') as f:
        f.write(audio_content)
    with open('video\\' + title + '.mp4', mode='wb') as f:
        f.write(video_content)


# response = get_response(html_url='https://www.bilibili.com/video/BV1AU4y1R7Uy')
# print(response)
video_info = get_video_info(play_url='https://www.bilibili.com/video/BV1yr4y1F7o2/?spm_id_from=autoNext')
save(video_info[0], video_info[1], video_info[2])
