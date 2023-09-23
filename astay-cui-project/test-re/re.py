import re

# 1.match 方法是从字符串开头开始匹配的，意味着一旦开头不匹配，整个匹配就失败了 取值用group()方法
content = 'Hello 123 4567 World_this is a regex demo'
print(len(content))
result_1 = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}', content)
# 正则解析
# ^表示匹配字符串的开头，\s表示匹配空白字符串，其实用来匹配hello后面的空格
# \d表示匹配数字，3个\d表示匹配123，后面四个数字可以用\d{4}来表示，\w{10}表示匹配10个字母以及下划线

print(result_1)
# group方法输出匹配到的内容
print(result_1.group())
# span方法输出匹配的范围
print(result_1.span())
# re.S的作用是使匹配内容包括换行符在内的所有字符
# re.I的作用是使匹配内容对大小写不敏感
result_2 = re.match('Hello(.*?)demo', content, re.S)
print(result_2)

# \为转义
content_01 = '(百度)www.baidu.com'
result_3 = re.match('\(百度\)www\.baidu\.com', content_01)
print(result_3)

# 2.search使用
result_4 = re.match('123\d{4}\s\w{10}', content)
result_5 = re.search('Hello (.*?) demo', content, re.S)
print(result_4)
print(result_5)

# 3.findall使用 返回的为取出的列表，所以在平时的使用中，最多的就是findall
result_6 = re.findall('Hello (.*?) demo', content, re.S)
print(result_6)
print(type(result_6))
result_7 = result_6[0]
print(result_7)

# 4.sub方法 在平时替换使用的时候用replace方法，但是过于繁琐，所以用sub也是一个好的选择
content_02 = '32hjDI234jBFk8s'
# 第一个参数\d+是传入所有的数字，第二个是要替换的参数，第三个为原字符串
content_02 = re.sub('\d+', '', content_02)
print(content_02)
# 当我们想拿到所有li节点的字时，可以使用sub先把所有a节点去掉 只留下文本 然后利用fandall进行提

# 5.compile方法 前面的方法都是用来处理字符串的，这个方法可以将正则字符串编译成正则表达式对象
content1 = '2022-7-26 11:11'
content2 = '2022-7-27 12:12'
content3 = '2022-7-28 13:13'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern, '', content1)
result2 = re.sub(pattern, '', content2)
result3 = re.sub(pattern, '', content3)
print(result1, result2, result3)
# 这个实例里有三个日期，我们想分别将这三个日期中的时间去掉，这是可以借助sub方法，该方法的第一个参数时正则表达式，但是没有必要重复写三个
# 这时可以借助compile方法将正则表达式编译成一个正则表达式对象，以便使用
# 另外 compile还可以传入修饰符，例如re.S等 这样在search，findall时就不用额外传了，可以说是compile方法给正则做了一层封装


