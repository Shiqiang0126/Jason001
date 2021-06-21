#cy3.py  @shiqiang 2019

import jieba
import wordcloud

f = open('实施乡镇振兴.txt','r',encoding='gbk')
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path = 'msyh.ttc',
                        width = 1000,  
                        height = 700,
                        background_color = 'white',
                        max_words = 15)
w.generate(txt)
w.to_file('grwordcloud.png')
