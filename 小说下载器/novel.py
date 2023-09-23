import requests
import parsel
from tqdm import tqdm


# 发送请求
def get_response(html_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    }
    response = requests.get(url=html_url, headers=headers)
    return response


# 解析所有章节
def get_chapter_url(list_url):
    list_data = get_response(html_url=list_url).text
    selector = parsel.Selector(list_data)
    href = selector.css('#list dd a::attr(href)').getall()
    novel_name = selector.css('#info h1::text').get()
    return href, novel_name


# 解析一章节数据
def get_novel_content(chapter_url):
    response = get_response(html_url=chapter_url)
    selector = parsel.Selector(response.text)
    chapter_title = selector.css('.bookname h1::text').get()
    content_list = selector.css('#content::text').getall() # getall()获取返回的为列表
    # '\n'.join(content_list) 相当于把列表中的每一个元素都用\n合并
    content = '\n'.join(content_list)
    return chapter_title, content


# 保存数据
def save(name, title, content):
    with open(name + '.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write(content)
        f.write('\n')


# 调用save函数保存数据
def main(num_id):
    novel_url = f'http://www.biqugse.com/{num_id}/'
    href, novel_name = get_chapter_url(list_url=novel_url)
    for link in tqdm(href):
        chapter_url = 'http://www.biqugse.com' + link
    chapter_title, content = get_novel_content(chapter_url=chapter_url)
    save(name=novel_name, title=chapter_title, content=content)
    print(novel_name, '下载完成')


if __name__ == '__main__':
    # url = 'http://www.biqugse.com/8820/30219252.html'
    # main(num_id=url)
    # url = 'http://www.biqugse.com/8820/'
    # get_chapter_url(list_url=url)
    main(num_id='8820')


