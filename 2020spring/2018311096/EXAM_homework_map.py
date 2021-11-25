# -*- coding:utf-8 -*-
#�������ǹ�óרҵ���Թ���ó�׸���Ȥ��������ȥ�о�һ�¸������Ҷ��й���ȡ�ķ�������ʩ��״���������ñ������ݿ�ѧ�ε�֪ʶ��һ����ͼ��������������Щ������û�������ϵĹ�ϵ,������ڳɹ����гɾ͸У�
#����һ��python�ļ�������һ�����Զ�������getcode�ĺ�������Ϊ�Ǹ�pygal�������Ҫ���Ҵ����Ӧ����
from EXAM_country_code_for_all import get_code
import matplotlib.pyplot as plt
import numpy as py
import pandas as pd
import pygal
#��ȡexcel�����ѹ��Ҷ�Ӧ����ת��Ϊ�ֵ�ļ���Ӧֵ
a=pd.read_excel('EXAM_AD_InitiationsRepMemVsExpCty.xls',sheet_name=0)
b=a.iloc[[0,15]].values
c=dict(zip(b[0],b[1]))
print(c)
#��鼼�����ޣ����ֶ�ɾ���ˣ���Щ�鷳
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
#���ֵ�ļ��滻����֮��Ӧ���б��һ�ַ��������ξ���Ϊ�ѹ������ƻ��ɹ��Ҵ���
print(c)
initiation_list=list(c.values())
d=[]
for country in c.keys():
	aa=get_code(country)
	d.append(aa)		
print(d)
e=dict(zip(d,initiation_list))
print(e)
#ɾ���б��е�ֵ�����ض������ļ�ֵ�ԣ�
l1={}
l2={}
for cyt,intt in e.items():
	if int(intt)==0:
		l1[cyt]=intt
	else:
		l2[cyt]=intt		
print(len(l1),len(l2))				
#���ӻ�
wm = pygal.maps.world.World()
wm.title = 'Anti-dumping initiations against China'
wm.add('suibianyigemingzi',l2)
#svgΪһ����վ�ļ�
wm.render_to_file('EXAM_initiation by regions.svg')

