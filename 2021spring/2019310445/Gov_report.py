# -*- coding: utf-8 -*-
"""
Created on Wed May 19 09:59:47 2021

@author: 皇后
统计2014-2021年政府工作报告词频矩阵
"""
# 调包
import re
import jieba
import matplotlib.pyplot as plt 
from collections import Counter #词频统计库
#import tools as t
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup as bs

plt.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示

# 爬取政府工作报告
def get_report(type="government"):
    '''
    http://www.gov.cn/guowuyuan/2020zfgzbg.htm 
    #2020年的政府工作报告长这样
    只有2014年以后的
    '''
    #爬取文件
    for year in range(2014,2022):
        news_url='http://www.gov.cn/guowuyuan/'+str(year)+'zfgzbg.htm' 
        r=requests.get(news_url,timeout=10)
        r.encoding='utf-8'
        s=bs(r.text,"html.parser")
        f=open(str(year)+"年政府工作报告.txt","w",encoding='utf-8')
        L=s.find_all("p")
        for c in L:
            f.write('{}\n'.format(c.text))   
        
        f.close()

    return 
# 从列表中统计词频数，返回频数列表
def get_freq(cleared_list):
    # keywords=open('keywords.txt','r',encoding='utf-8').readlines().strip() #返回一个list
    keywords=[line.replace('\n','') for line in open("keywords.txt",encoding="utf-8").readlines()]
    
    # 开始统计词频
    yearly_list=[0]*len(keywords)
    i=0
    for kw in keywords:
        for word in cleared_list:
            if word == kw:
                yearly_list[i]+=1
        i+=1
    return yearly_list

def report_freq():      
    # 先生成预备矩阵
    keywords=[line.replace('\n','') for line in open("keywords.txt",encoding="utf-8").readlines()]
    df=pd.DataFrame(index=list(range(2014,2021)),
                    columns=keywords)
    # 遍历处理文件
    for year in range(2014,2022):
        f=open(str(year)+"年政府工作报告.txt","r",encoding='utf-8')
        
        # 文本预处理
        pattern = re.compile('[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？“”、~@#￥%……&*（）(\d+)]+')
        string_data=re.sub(pattern,'',f.read()) # 符合模式的字符去除
        # 文本分词：全模式
        seg_list=jieba.cut(string_data)
        # 清洗垃圾词
        cleared_list=[]
        remove_words = [u'的',u'要', u'“',u'”',u'和',u'，',u'为',u'是',
                u'以' u'随着', u'对于', u'对',u'等',u'能',u'都',u'。',
                u' ',u'、',u'中',u'在',u'了',u'通常',u'如果',u'我',
                u'她',u'（',u'）',u'他',u'你',u'？',u'—',u'就',
                u'着',u'说',u'上',u'这', u'那',u'有', u'也',
                u'什么', u'·', u'将', u'没有', u'到', u'不', u'去'] 
        for word in seg_list:
            if word not in remove_words:
                cleared_list.append(word)
        # print(cleared_list[0:10])
        
        # 统计最高词频数
        temp_freq=get_freq(cleared_list)
        df.loc[year]=temp_freq
        
        f.close()
    
    # print(df)
    # 保存到Excel
    df.to_excel("keywords_of_gov_report.xlsx")
    return df


# 展示词频矩阵结果
def plot_report(data,graph_type='line'):
    
    return

#主函数
def main():
    get_report()
    report_freq()
    return

if __name__=='__main__':
    main()