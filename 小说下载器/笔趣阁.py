import requests
import parsel
from tqdm import tqdm

url = 'http://biqugse.com/8820/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response = requests.get(url, headers).text
selector = parsel.Selector(response)
novel_name = selector.css('#info h1::text').get()
detail_href = selector.css('#list dd a::attr(href)').getall()[9:625]
for href in tqdm(detail_href):
    list_url = 'http://biqugse.com' + href
    # print(list_url)
    data_details = requests.get(url=list_url, headers=headers).text
    selectors = parsel.Selector(data_details)
    title = selectors.css('.bookname h1::text').get()
    content_list = selectors.css('#content::text').getall()  # getall()获取返回的为列表
    # '\n'.join(content_list) 相当于把列表中的每一个元素都用\n合并
    content = '\n'.join(content_list)
    # print(content)
    with open(novel_name + '.txt', mode='a', encoding='utf-8') as f:
        f.write(title)
        f.write(content)
        f.write('\n')

