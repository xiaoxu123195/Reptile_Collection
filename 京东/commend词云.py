import jieba
from wordcloud import wordcloud

f = open('Wcloudcomment.txt', encoding='utf-8')
text = f.read()
# print(text)
string = ' '.join(jieba.lcut(text))
# print(string)
wc = wordcloud.WordCloud(
    width=1000,
    height=700,
    font_path='msyh.ttc'
)

wc.generate(string)
wc.to_file('词云.png')
