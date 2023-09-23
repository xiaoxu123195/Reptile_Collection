# 处理sign
import execjs
# d.token + "&" + i + "&" + g + "&" + c.data
import time

token = '7c6ad9e919583e6487aab1f8d9933b2a'
i = round(time.time() * 1000)
g = '12574478'
data = '{"cid":"FactoryRankServiceWidget:FactoryRankServiceWidget","methodName":"execute","params":"{\\"extParam\\":{\\"methodName\\":\\"readRelatedRankEntries\\",\\"cateId\\":\\"\\",\\"size\\":15},\\"url\\":\\"https://factory.1688.com/index.html\\"}"}'


signKey = token + "&" + str(i) + "&" + g + "&" + data
with open('./123.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

ctx = execjs.compile(jscode).call('h', signKey)
print(ctx)
