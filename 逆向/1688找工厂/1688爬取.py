import execjs
import time

import requests

token = '7c6ad9e919583e6487aab1f8d9933b2a'
i = round(time.time() * 1000)
g = '12574478'
data = '{"cid":"FactoryRankServiceWidget:FactoryRankServiceWidget","methodName":"execute","params":"{\\"extParam\\":{\\"methodName\\":\\"readRelatedRankEntries\\",\\"cateId\\":\\"\\",\\"size\\":15},\\"url\\":\\"https://factory.1688.com/index.html\\"}"}'

signKey = token + "&" + str(i) + "&" + g + "&" + data
with open('./123.js', 'r', encoding='utf-8') as f:
    jscode = f.read()
ctx = execjs.compile(jscode).call('h', signKey)

params = {
    'jsv': '2.4.11',
    'appKey': '12574478',
    't': i,
    'sign': ctx,
    'v': '1.0',
    'type': 'jsonp',
    'isSec': 0,
    'timeout': 20000,
    'api': 'mtop.taobao.widgetService.getJsonComponent',
    'dataType': 'jsonp',
    'jsonpIncPrefix': 'mboxfc',
    'callback': 'mtopjsonpmboxfc7',
    'data': data,
}

url = 'https://h5api.m.1688.com/h5/mtop.taobao.widgetservice.getjsoncomponent/1.0/?'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'referer': 'https://factory.1688.com/',
    'cookie': 'cna=dQMJGmGeEBgCAd2wnMwi9Et6; cookie2=1b517af099409fb7f65adb4c27f818c1; sgcookie=E100Eljj3M86titZrNe%2FFlHEOTpwB%2F8lvIwFmJyf6TgrcWykJVh3saV2sLsWyAb8qJuVtQorQ0PgDWcpOf%2BpX9tgWeyiWPfzG5bGzLxlVnCghKu1KAfVJsw1NHg5UZyMa7v2; t=0a7c07885539d5762b1fe1c12b4c23d0; _tb_token_=8fe6e8e67107; __cn_logon__=false; xlly_s=1; _m_h5_tk=7c6ad9e919583e6487aab1f8d9933b2a_1658915674799; _m_h5_tk_enc=2a164be0bb4007225f9c1a4991fb12c8; alicnweb=touch_tb_at%3D1658905240669; tfstk=cgu1Bd2DLOX66bJQLlOe0spAIo41Z1f7Ghwi1pfePVy617c1iYbzFNfnmtU4MW1..; l=eBT69FV7L9NC0M8NKOfwnurza77tTIRfguPzaNbMiOCP_WCk53vFW6xxwtTDCnGVH65DR3Wrj_IwBKMWqydVCoxLre_gstgqndC..; isg=BOHh1714J1ALroskUfU5nWcd8K37jlWAlL-KHUO2iuheqgB8i95LUOfsDN4sYu24'
}
response = requests.get(url, headers=headers, params=params).text
print(response)


