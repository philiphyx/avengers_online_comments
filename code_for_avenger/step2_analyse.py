#https://blog.csdn.net/qq_41816368/article/details/81073215
import re
import jieba
import pandas as pd
import numpy as np
from scipy.misc import imread
import matplotlib.pyplot as plt
from wordcloud import WordCloud  # 词云包
import matplotlib
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

f = open('movie_comments.txt', 'r', encoding='utf-8')
content = f.read()
pattern = re.compile(r'[\u4e00-\u9fa5]+')
filterdata = re.findall(pattern, content)
#print(filterdata)
cleaned_comments = ''.join(filterdata)

segment = jieba.lcut(cleaned_comments)
#print(segment)
segment = list(segment)    #转换成list！！！！
words_df = pd.DataFrame({'segment': segment})


#print(words_df.head())
stopwords = pd.read_csv("stopwords.txt", index_col=False, quoting=3, sep="\t", names=['stopword'],
                        encoding='utf-8')  # quoting=3全不引用
#  去除停用词
words_df = words_df[~words_df.segment.isin(stopwords.stopword)]


# print(words_df.head())
words_stat = words_df.groupby(by=['segment'])['segment'].agg({"计数": np.size})
words_stat = words_stat.reset_index().sort_values(by=["计数"], ascending=False)
print(words_stat.head(50))  #  头5行展示
print(words_stat)       #所有词展示

#######################
color_mask = imread("love.jpg")
##############
matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
wordcloud = WordCloud(font_path="simhei.ttf", background_color="white", max_font_size=80,mask=color_mask,)  # 指定字体类型、字体大小和字体颜色
word_frequence = {x[0]: x[1] for x in words_stat.head(1000).values}
#   0 是词语  键  1 是计数 值
print(word_frequence)
print(type(word_frequence))   #  类型是字典

word_frequence_list = []
for key in word_frequence:
    temp = (key, word_frequence[key])
    word_frequence_list.append(temp)

print(word_frequence_list)
print(type(word_frequence_list))   ##  类型是列表

wordcloud = wordcloud.fit_words(dict(word_frequence_list))



##########################################
###########color_mask = imread("love.jpg")
image_colors = ImageColorGenerator(color_mask)


# 显示图片
plt.imshow(wordcloud)
plt.axis("off")
# 绘制词云


# plt.figure()  #创建了一个空的图像窗口,重新染色
# plt.imshow(wordcloud.recolor(color_func=image_colors))
# plt.axis("off")


# plt.figure()
# plt.imshow(color_mask, cmap=plt.cm.gray)
# plt.axis("off")


plt.show()
# 保存图片
wordcloud.to_file("love_in.jpg")

#########################################
#plt.imshow(wordcloud)
#plt.show()
f.close()