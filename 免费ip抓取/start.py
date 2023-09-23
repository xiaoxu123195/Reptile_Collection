import requests
import parsel
import json

proxies_list = []
proxies_list_1 = []

for page in range(1, 11):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

    url = f"https://free.kuaidaili.com/free/inha/{page}/"
    response = requests.post(url, headers=headers)

    selector = parsel.Selector(response.text)
    trs = selector.css('#list > table > tbody > tr')
    for tr in trs:
        ip_num = tr.css('td:nth-child(1)::text').get()
        # ip_num = tr.xpath('td[1]/text()').get()
        ip_port = tr.css('td:nth-child(2)::text').get()

        proxies_dict = {
            "http": "http://" + ip_num + ":" + ip_port,
            "https": "http://" + ip_num + ":" + ip_port,
        }

        # print(proxies_dict)
        # 检测ip是否可用
        # timeout = 1 是响应超过一秒的都直接past
        proxies_list_1.append(proxies_dict)
        try:
            response_1 = requests.get(url='https://www.baidu.com/', proxies=proxies_dict, timeout=1)
            if response_1.status_code == 200:
                proxies_list.append(proxies_dict)
                print(proxies_dict, '代理可以使用')
                with open('代理.txt', mode='a', encoding='utf-8') as f:
                    f.write(json.dumps(proxies_dict))
                    f.write('\n')
        except:
            print('当前代理', proxies_dict, '不合格')

print('-*-*-' * 30)
print('一共获取到：', len(proxies_list_1), '个代理')
print('可以使用：', len(proxies_list), '个代理')
print(proxies_list)

'''
    ip代理的结构为
    proxies_dict = {
        "http": "http://" + ip:端口,
        "https": "http://" + ip:端口,
    }
'''
