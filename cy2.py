import jieba #引入第三方分词库
import wordcloud
txt = "程序设计语言是计算机能够理解和识别用户操作意图的一种交互体系，能够，能够，它按照特定规则组织计算机指令，使计算机能够自动进行各种运算处理。"
w = wordcloud.WordCloud( width=1000,font_path="msyh.ttc",height=700) #改变了缺省参数，包括输出的长宽像素，选用字体
w.generate(" ".join(jieba.lcut(txt))) #利用分词库，把文本中的汉字分词后用空格隔开
w.to_file("pywcloud.png")
