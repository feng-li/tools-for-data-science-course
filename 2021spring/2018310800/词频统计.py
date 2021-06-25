import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from snownlp import SnowNLP
import jieba
import jieba.posseg as psg
from collections import Counter
import jieba.analyse

list_brand = ["小米","华为","魅族","OPPO","VIVO","苹果"]
list_APP = ["TIM","WPS","ZOOM","百度网盘","钉钉","抖音","飞书","企业微信","腾讯会议","学习通"]#王者荣耀

file_list = []
str_APP = "TIM"
print("=====开始读取"+str_APP)
file_list.append(pd.read_excel('时间数据/'+str_APP+'格式化时间数据.xlsx')) 
print("=====读取完毕=====")

comments = []
for i,j,k in zip(file_list[0]["删除"],file_list[0]["内容"],file_list[0]["星级"]):
    if i == False:
        #print(i,j,k)
        comments.append([k,j])
    else:
        pass
        
for i in comments:
    cut_result = jieba.cut(str(i[1]),use_paddle=True)
    #print(i[0],"/".join(cut_result))
    
jieba.analyse.set_stop_words('stopwords.txt')
segments = []
for i in comments:
    content = i[1]
    #TextRank 关键词抽取，只获取固定词性
    words = jieba.analyse.textrank(str(content), topK=20,withWeight=False,allowPOS=('ns', 'n', 'vn', 'v'))
    splitedStr = ''
    for word in words:
        # 记录全局分词
        segments.append({'word':word, 'count':1})
        splitedStr += word + ' '


# 将结果数组转为df序列
dfSg = pd.DataFrame(segments)

# 词频统计
dfWord = dfSg.groupby('word')['count'].sum()

print(dfSg,dfWord)

import re
frq_all = []
for i in comments[0:20]:
    frq_s = []
    for j in dfSg["word"]:
        if re.search(str(j),str(i[1])):
            frq_s.append(1)
        else:
            frq_s.append(0)
    frq_all.append(frq_s)


print(len(frq_all))
for i in frq_all:
    print(i,"\n"
