#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from datetime import datetime
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']


# In[2]:


data0 = pd.read_excel("E:/360MoveData/Users/Lenovo/Desktop/韩晓龙/个人资料 _ Twitter——.xlsx")


# In[3]:


data0


# In[4]:


#根据推文去重
data = data0.drop_duplicates("推文")


# In[5]:


data = data.reset_index(drop = True)
data


# In[7]:





# In[6]:


#数据清洗
for j in range(0,len(data)):
    if type(data['评论数'][j]) == str:
        if '万' in data['评论数'][j]:
            data['评论数'][j] = int(float(re.findall(r"\d+\.?\d*",data['评论数'][j])[0])*10000)
        else:    
            a = re.findall(r"\d+\.?\d*",data['评论数'][j])
            m = 0
            if len(a)>1:
                for i in range(1,len(a)+1):    
                    m += int(a[len(a)-i])*(1000**(i-1))
                data['评论数'][j] = m
            else:
                data['评论数'][j] = int(a[0])

for j in range(0,len(data)):
    if type(data['转发数'][j]) == str:
        if '万' in data['转发数'][j]:
            data['转发数'][j] = int(float(re.findall(r"\d+\.?\d*",data['转发数'][j])[0])*10000)
        else:    
            a = re.findall(r"\d+\.?\d*",data['转发数'][j])
            m = 0
            if len(a)>1:
                for i in range(1,len(a)+1):    
                    m += int(a[len(a)-i])*(1000**(i-1))
                data['转发数'][j] = m
            else:
                data['转发数'][j] = int(a[0])

for j in range(0,len(data)):
    if type(data['点赞数'][j]) == str:
        if '万' in data['点赞数'][j]:
            data['点赞数'][j] = int(float(re.findall(r"\d+\.?\d*",data['点赞数'][j])[0])*10000)
        else:    
            a = re.findall(r"\d+\.?\d*",data['点赞数'][j])
            m = 0
            if len(a)>1:
                for i in range(1,len(a)+1):    
                    m += int(a[len(a)-i])*(1000**(i-1))
                data['点赞数'][j] = m
            else:
                data['点赞数'][j] = int(a[0])


# In[7]:


data


# In[57]:


#数据可视化
plt.figure(figsize=(14,5))#设置画布
plt.plot(data['时间'],data['评论数'],linestyle = '-',c = 'red',marker = '+',label = '评论数')
plt.plot(data['时间'],data['转发数'],linestyle = '-.',c = 'orange',marker = '.',label = '转发数')
#plt.plot(data['时间'],data['点赞数'],linestyle = '--',c = 'yellow',label = '点赞数')

plt.xlabel('时间')
plt.ylabel('数值')
plt.title('各条推文转发数、评论数折线图')
plt.savefig('各条推文转发数、评论数折线图.png')
plt.legend()
plt.show()


# In[58]:


plt.figure(figsize=(14,5))#设置画布
plt.plot(data['时间'],data['点赞数'],linestyle = '--',marker = '+',c = 'yellow')
plt.xlabel('时间')
plt.ylabel('点赞数')
plt.title('各条推文点赞数折线图')
plt.savefig('各条推文点赞数折线图.png')

plt.show()


# In[9]:


month = pd.DataFrame(columns = ['月份','总发帖数','总点赞数','总转发数','总评论数'])
month['月份'] = ['一月','二月','三月','四月']
month['总发帖数'] = 0
month['总点赞数'] = 0
month['总转发数'] = 0
month['总评论数'] = 0
month


# In[10]:


for i in range(0,len(data)):
    if data['时间'][i].month == 1:
        month['总发帖数'][0] += 1
        month['总点赞数'][0] += data['点赞数'][i]
        month['总转发数'][0] += data['转发数'][i]
        month['总评论数'][0] += data['评论数'][i]
    elif data['时间'][i].month == 2:
        month['总发帖数'][1]+= 1
        month['总点赞数'][1]+= data['点赞数'][i]
        month['总转发数'][1]+= data['转发数'][i]
        month['总评论数'][1]+= data['评论数'][i]
    elif data['时间'][i].month == 3:
        month['总发帖数'][2]+= 1
        month['总点赞数'][2]+= data['点赞数'][i]
        month['总转发数'][2]+= data['转发数'][i]
        month['总评论数'][2]+= data['评论数'][i]
    elif data['时间'][i].month == 4:
        month['总发帖数'][3]+= 1
        month['总点赞数'][3]+= data['点赞数'][i]
        month['总转发数'][3]+= data['转发数'][i]
        month['总评论数'][3]+= data['评论数'][i]


# In[11]:


month


# In[56]:


#整体绘图
plt.figure(figsize=(14,5))#设置画布
plt.plot(month['月份'],month['总评论数']/month['总发帖数'],linestyle = '-',c = 'red',marker = '+',label = '月均评论数')
plt.plot(month['月份'],month['总转发数']/month['总发帖数'],linestyle = '-.',c = 'orange',marker = '.',label = '月均转发数')
plt.plot(month['月份'],month['总点赞数']/month['总发帖数'],linestyle = '--',c = 'yellow',label = '月均点赞数')

for a, b in zip(month['月份'], round(month['总评论数']/month['总发帖数'])):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(month['月份'], round(month['总转发数']/month['总发帖数'])):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
for a, b in zip(month['月份'], round(month['总点赞数']/month['总发帖数'])):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.xlabel('月份')
plt.ylabel('数值')
plt.title('月均推文转发数、评论数、点赞数折线图')
plt.savefig('月均推文转发数、评论数、点赞数折线图.png')
plt.legend()
plt.show()


# In[13]:


label = month['月份']#刻度标签
plt.figure(figsize=(14,5))#设置画布
plt.bar(range(4),month['总发帖数'],width= 0.5)
plt.xlabel('月份')
plt.ylabel('总发帖数')
plt.xticks(range(4),label)
plt.title('各月发帖频数统计直方图')
for a, b in zip(range(4), month['总发帖数']):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig('各月发帖频数统计直方图.png')
plt.show()
print('---------------------------------------')


# In[17]:


a = list(data['是否为转推']).count(data['是否为转推'][0])
len(data)
value = [a,len(data)-a]
value


# In[18]:


label = ['转推','自创']#刻度标签
explode = [0.01,0.01]
pl = plt.figure(figsize=(6,12))#设置画布

plt.pie(value,explode = explode,labels = label,
       autopct = '%1.1f%%')
plt.title('推文属性饼图')
plt.savefig('推文属性饼图饼图.png')
plt.show()


# In[19]:


send = []
for i in range(0,len(data)):
    if data['是否为转推'][i] == data['是否为转推'][0]:
        send.append(data['转推自'][i])


# In[20]:


result = pd.value_counts(send)
result.index


# In[21]:


label = result.index#刻度标签
pl = plt.figure(figsize=(6,12))#设置画布
plt.pie(result,labels = label,
       autopct = '%1.1f%%')
plt.title('转发推送属性饼图')
plt.savefig('转发推送饼图饼图.png')
plt.show()


# In[13]:


text1 = ''
text2 = ''
text3 = ''
text4 = ''
for i in range(0,len(data)):
    if data['时间'][i].month == 1:
        text1 +=' '+data['推文'][i]
    elif data['时间'][i].month == 2:
        text2 += ' '+data['推文'][i]
    elif data['时间'][i].month == 3:
        text3 += ' '+data['推文'][i]
    elif data['时间'][i].month == 4:
        text4 += ' '+data['推文'][i]


# In[59]:





# In[25]:


import re
from nltk.corpus import stopwords
from nltk import word_tokenize,pos_tag 
from gensim import corpora,models
from nltk.stem import PorterStemmer


# In[15]:


stop_words = set(stopwords.words('english')) 


# In[41]:


#去停用词
cutwords1 = word_tokenize(text1)
interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','’','—','I','We']   #定义标点符号列表
cutwords1 = [word for word in cutwords1 if word not in interpunctuations]   #去除标点符号
stops = set(stopwords.words("english"))
cutwords1 = [word for word in cutwords1 if word not in stops]  #判断分词在不在停用词列表内
print('\n【NLTK分词后去除停用词结果：】')
print(cutwords1)


# In[24]:


PorterStemmer().stem('i')


# In[42]:


dic = {}
for word in cutwords2:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1

swd = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

stop_words = set(stopwords.words('english')) 
i = 0
for k,v in swd:
    if k in stop_words:
        swd.pop(i)
    i += 1


# In[43]:


swd


# In[44]:


key = [None]*10
value = [0]*10
a=None
i=0
for k,v in swd[:10]:
    key[i] = k
    value[i] = v
    i = i+1


# In[59]:


label = key#刻度标签
plt.figure(figsize=(14,5))#设置画布
plt.bar(range(10),value,width= 0.5)
plt.xlabel('词语')
plt.ylabel('词频')
plt.xticks(range(10),label)
plt.title('一月发帖词频统计直方图')
for a, b in zip(range(10), value):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig('一月发帖词频统计直方图.png')
plt.show()


# In[61]:


#去停用词
cutwords2 = word_tokenize(text2)
interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','’','—','I','We']   #定义标点符号列表
cutwords2 = [word for word in cutwords2 if word not in interpunctuations]   #去除标点符号
stops = set(stopwords.words("english"))
cutwords2 = [word for word in cutwords2 if word not in stops]  #判断分词在不在停用词列表内


# In[62]:


dic = {}
for word in cutwords2:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1

swd = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

stop_words = stopwords.words('English')
i=0
for k,v in swd:
    if k in stop_words:
        swd.pop(i)
    i += 1
key = [None]*10
value = [0]*10
a=None
i=0
for k,v in swd[:10]:
    key[i] = k
    value[i] = v
    i = i+1

label = key#刻度标签
plt.figure(figsize=(14,5))#设置画布
plt.bar(range(10),value,width= 0.5)
plt.xlabel('词语')
plt.ylabel('词频')
plt.xticks(range(10),label)
plt.title('二月发帖词频统计直方图')
for a, b in zip(range(10), value):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig('二月发帖词频统计直方图.png')
plt.show()


# In[63]:


#去停用词
cutwords3 = word_tokenize(text3)
interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','’','—','I','We']   #定义标点符号列表
cutwords3 = [word for word in cutwords3 if word not in interpunctuations]   #去除标点符号
stops = set(stopwords.words("english"))
cutwords3 = [word for word in cutwords3 if word not in stops]  #判断分词在不在停用词列表内


# In[64]:


dic = {}
for word in cutwords3:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1

swd = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

stop_words = stopwords.words('English')
i=0
for k,v in swd:
    if k in stop_words:
        swd.pop(i)
    i += 1
key = [None]*10
value = [0]*10
a=None
i=0
for k,v in swd[:10]:
    key[i] = k
    value[i] = v
    i = i+1

label = key#刻度标签
plt.figure(figsize=(14,5))#设置画布
plt.bar(range(10),value,width= 0.5)
plt.xlabel('词语')
plt.ylabel('词频')
plt.xticks(range(10),label)
plt.title('三月发帖词频统计直方图')
for a, b in zip(range(10), value):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig('三月发帖词频统计直方图.png')
plt.show()


# In[65]:


#去停用词
cutwords4 = word_tokenize(text4)
interpunctuations = [',', '.', ':', ';', '?', '(', ')', '[', ']', '&', '!', '*', '@', '#', '$', '%','-','’','—','I','We']   #定义标点符号列表
cutwords4 = [word for word in cutwords4 if word not in interpunctuations]   #去除标点符号
stops = set(stopwords.words("english"))
cutwords4 = [word for word in cutwords4 if word not in stops]  #判断分词在不在停用词列表内


# In[66]:


dic = {}
for word in cutwords4:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1

swd = sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse = True)

stop_words = stopwords.words('English')
i=0
for k,v in swd:
    if k in stop_words:
        swd.pop(i)
    i += 1
key = [None]*10
value = [0]*10
a=None
i=0
for k,v in swd[:10]:
    key[i] = k
    value[i] = v
    i = i+1

label = key#刻度标签
plt.figure(figsize=(14,5))#设置画布
plt.bar(range(10),value,width= 0.5)
plt.xlabel('词语')
plt.ylabel('词频')
plt.xticks(range(10),label)
plt.title('四月发帖词频统计直方图')
for a, b in zip(range(10), value):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=10)
plt.savefig('四月发帖词频统计直方图.png')
plt.show()


# In[55]:


words_ls = [cutwords1,cutwords2,cutwords3,cutwords4]
#去重，存到字典
dictionary = corpora.Dictionary(words_ls)
#print(dictionary)
corpus = [dictionary.doc2bow(words) for words in words_ls]
#print(corpus)
lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=4)
for topic in lda.print_topics(num_words=10):
    print(topic)

