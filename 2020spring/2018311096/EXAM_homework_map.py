# -*- coding:utf-8 -*-
#由于我是国贸专业，对国际贸易感兴趣，所以想去研究一下各个国家对中国采取的反倾销措施的状况，很想用本次数据科学课的知识把一个热图做出来，看看这些国家有没有区域上的关系,最后终于成功很有成就感！
#从另一个python文件引入了一个我自定的名叫getcode的函数，因为那个pygal库必须需要国家代码对应起来
from EXAM_country_code_for_all import get_code
import matplotlib.pyplot as plt
import numpy as py
import pandas as pd
import pygal
#读取excel，并把国家对应数据转换为字典的键对应值
a=pd.read_excel('EXAM_AD_InitiationsRepMemVsExpCty.xls',sheet_name=0)
b=a.iloc[[0,15]].values
c=dict(zip(b[0],b[1]))
print(c)
#这块技术有限，就手动删除了，有些麻烦
del c['Exporter']
del c['Total']
del c['Eswatini']
del c['Kyrgyz']
del c['Saudi Arabia, Kingdom of']
del c['Taipei, Chinese']
del c['Trinidad and Tobago']
del c['Qatar']
del c["European Union"]
eu=['France','Germany','Italy','Netherlands','Belgium','Britain',
'Denmark','Ireland','Greece','Portugal','Spain','Austria','Sweden','Finland','Malta','Cyprus','Poland']
for i in eu:
	c[i]=8
#把字典的键替换成与之对应的列表的一种方法，本次具体为把国家名称换成国家代码
print(c)
initiation_list=list(c.values())
d=[]
for country in c.keys():
	aa=get_code(country)
	d.append(aa)		
print(d)
e=dict(zip(d,initiation_list))
print(e)
#删除列表中的值满足特定条件的键值对！
l1={}
l2={}
for cyt,intt in e.items():
	if int(intt)==0:
		l1[cyt]=intt
	else:
		l2[cyt]=intt		
print(len(l1),len(l2))				
#可视化
wm = pygal.maps.world.World()
wm.title = 'Anti-dumping initiations against China'
wm.add('suibianyigemingzi',l2)
#svg为一种网站文件
wm.render_to_file('EXAM_initiation by regions.svg')

