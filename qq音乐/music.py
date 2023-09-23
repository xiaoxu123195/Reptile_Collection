#  https://aqqmusic.tc.qq.com/amobile.music.tc.qq.com/C400003UkWuI0E8U0l.m4a?guid=8338016672&vkey=6FAB55E8BFF1B2401A732D6B10E7BFDB82A86B717CB8EE8AB8466848A9ADC7672AED78CB434F3B54E39AD85200DBCC577E35692058A42F2F&uin=&fromtag=123032

import requests


url = ' https://aqqmusic.tc.qq.com/amobile.music.tc.qq.com/C400003UkWuI0E8U0l.m4a?guid=8338016672&vkey=6FAB55E8BFF1B2401A732D6B10E7BFDB82A86B717CB8EE8AB8466848A9ADC7672AED78CB434F3B54E39AD85200DBCC577E35692058A42F2F&uin=&fromtag=123032'

response = requests.get(url=url)
# response.content

with open('孤勇者.mp3', mode='wb') as f:
    f.write(response.content)
