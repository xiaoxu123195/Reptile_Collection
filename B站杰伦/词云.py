import jieba
import wordcloud

f = open('弹幕.txt', encoding='utf-8')
txt = f.read()
# print(txt)
string = ' '.join(jieba.lcut(txt))
# print(string)
wc = wordcloud.WordCloud(
    width=700,
    height=700,
    background_color='white',
    font_path='msyh.ttc',  # 设置字体
    scale=10,  # 规模大小
)
wc.generate(string)
wc.to_file('1.png')
