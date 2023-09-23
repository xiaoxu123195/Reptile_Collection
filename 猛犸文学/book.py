import requests
import re

url = 'https://www.shanghairanking.cn/_nuxt/static/1663839122/rankings/bcur/2022/payload.js'

headers = {
    'referer': 'https://www.shanghairanking.cn/rankings/bcur/2022',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'cookie': 'Hm_lvt_af1fda4748dacbd3ee2e3a69c3496570=1664843159; Hm_lpvt_af1fda4748dacbd3ee2e3a69c3496570=1664843443'
}

response = requests.get(url, headers=headers).text
a = re.findall('univData:(.*?)', response)
print(response)
print(a)


