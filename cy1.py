import wordcloud
txt = "life is short, you need python" 
w = wordcloud.WordCloud() #建立词云对象，全部使用缺省参数配置
w.generate(txt) #加载文本，用以产生词云
w.to_file("pywcloud.png") #输出为图片文件，png jpg 可选
