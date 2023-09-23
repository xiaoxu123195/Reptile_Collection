import requests
import execjs
import random
import time
import pprint

e = input('enter the english world:')
# time.time() 时间戳，python的时间戳*1000是js的时间戳 int是取整数  使用str转成字符串 才能进行拼接
# random.random() 随机生成的为0.几
r = str(int(time.time() * 1000))  # js时间戳
i = r + str(int(random.random() * 10))

node = execjs.get()
ctx = node.compile(open('./翻译.js', encoding='utf-8', ).read())
funcName = "getSign('{0}','{1}')".format(e, i)
sign = ctx.eval(funcName)
# print(sign)
url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 '
                  'Safari/537.36 ',
    'Referer': 'https://fanyi.youdao.com/',
    'Cookie': 'OUTFOX_SEARCH_USER_ID=1276541417@10.105.137.204; OUTFOX_SEARCH_USER_ID_NCOO=760551964.0892303; '
              'fanyi-ad-id=307888; fanyi-ad-closed=1; ___rl__test__cookies=1657880049250 ',
}
data = {
    'i': e,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': i,
    'sign': sign,
    'lts': r,
    'bv': 'f0819a82107e6150005e75ef5fddcc3b',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME',
}
result = requests.post(url, headers=headers, data=data).json()
# print(result)
# pprint.pprint(result)
# noun1 = result['smartResult']['entries'][0]
# noun2 = result['smartResult']['entries'][1]
# noun = noun1 + noun2
# verb = result['smartResult']['entries'][2]
# print(noun, verb)
last = result['smartResult']['entries']
for i in last:
    print(i)
