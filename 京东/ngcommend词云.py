import jieba
from wordcloud import wordcloud

f = open('Wcloudngcomment.txt', encoding='utf-8')
text = f.read()
# print(text)
string = ' '.join(jieba.lcut(text))
# print(string)
wc = wordcloud.WordCloud(
    width=1000,
    height=700,
    font_path='msyh.ttc',
    stopwords={'的','了','手机','买','不','就','没有'}
)

wc.generate(string)
wc.to_file('ng词云.png')