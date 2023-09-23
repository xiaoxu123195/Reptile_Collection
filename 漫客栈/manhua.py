import requests
import parsel
import os

headers = {
    'referer': 'https://www.mkzhan.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

link = 'https://www.mkzhan.com/214233/'
response_1 = requests.get(url=link, headers=headers).text
sel = parsel.Selector(response_1)
lis = sel.css('div.de-chapter > div.chapter__list.clearfix > ul > li')
name = sel.css(' div.de-info-wr > div.container--response > div > p::text').get()
for li in list(reversed(lis)):
    chapter_id = li.css('a::attr(data-chapterid)').get()
    chapter_name = li.css('a::text').getall()[-1].strip()
    file = f'{name}\\{chapter_name}\\'
    if not os.path.exists(file):
        os.makedirs(file)

    url = 'https://comic.mkzcdn.com/chapter/content/v1/'
    data = {
        'chapter_id': chapter_id,
        'comic_id': '214233',
        'format': '1',
        'quality': '1',
        'sign': '9d6b767613407f29faa9fb1741aa716a',
        'type': '1',
        'uid': '56778117',
    }
    response = requests.get(url, params=data, headers=headers).json()
    page = response['data']['page']
    num = 1
    for index in page:
        img_url = index['image']
        img_content = requests.get(url=img_url, headers=headers).content
        with open(file + chapter_name + str(num) + '.jpg', mode='wb') as f:
            f.write(img_content)
        num += 1
        print(img_url)
