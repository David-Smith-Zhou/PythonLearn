# -*- coding: utf-8 -*- f
#encoding=gbk
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# 获取当前路径，亲测两种都行
# d = path.dirname(__file__)
d = path.dirname('.')

# 读取文字
"""
Project Gutenberg's Alice's Adventures in Wonderland, by Lewis Carroll

This eBook is for the use of anyone anywhere at no cost and with
almost no restrictions whatsoever.  You may copy it, give it away or
re-use it under the terms of the Project Gutenberg License included
with this eBook or online at www.gutenberg.org
"""

text = open(path.join(d, 'alice.txt')).read()

# 设置背景图片
alice_coloring = imread(path.join(d, 'pikatiu.jpg'))


wc = WordCloud(background_color="white",            # 背景颜色，
               max_words=2000,                      # 词云显示的最大词数
               mask=alice_coloring,                 # 设置背景图片
               stopwords=STOPWORDS.add("said"),     #
               max_font_size=100,                   # 字体最大值
               random_state=21)                     # 随机种子
# 生成词云
wc.generate(text)
# 从背景图片生成颜色值
image_colors = ImageColorGenerator(alice_coloring)

# 显示图片
plt.imshow(wc)
plt.axis("off")
# 绘制词云
plt.figure()
plt.imshow(wc.recolor(color_func=image_colors))
plt.axis("off")
plt.figure()
plt.imshow(alice_coloring, cmap=plt.cm.gray)
plt.axis("off")
plt.show()
# 保存图片
wc.to_file(path.join(d, "mingcheng.png"))