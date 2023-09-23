# 如果需要逆向的js函数的实现是出现在一个闭包中，那么直接将闭包的整个代码块拷贝出进行调试即可
import execjs
# 实例化一个node对象
node = execjs.get()
# js源文件编译
ctx = node.compile(open('./login.js', encoding='utf-8').read())
# 执行js函数
funcName = 'md5("{0}")'.format('123456')
pwd = ctx.eval(funcName)
print(pwd)
