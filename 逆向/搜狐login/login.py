import execjs


password = input("请输入密码:")

with open('./123.js', 'r', encoding='utf-8') as f:
    jscode = f.read()

# s是要执行的函数 data是加密的数据 ctx = execjs.compile(jscode).call('s', data)
ctx = execjs.compile(jscode).call('md5', password)
print(ctx)
