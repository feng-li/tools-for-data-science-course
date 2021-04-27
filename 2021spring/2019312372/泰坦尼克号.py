#sex age
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
data = pd.read_csv('./titanic.csv')
data.info()
########
print("乘客的存活情况(条形图)")
data_survived = data[data['survived']==1]['row.names'].count()
data_not_survived = data[data['survived']==0]['row.names'].count()
print('生还者有{0}人,遇难者有{1}人'.format(data_survived, data_not_survived))
#生还者有449人,遇难者有864人
plt.figure(figsize=(10,4),dpi=80)
plt.subplot(121)
#sns.countplot(x='survived',data=data)
sns.countplot(data['survived'])
plt.title('survived count')

#plt.subplot(122)
#data.groupby('survived').count()['row.names'].plot(kind='bar')
#plt.title('survived count')
plt.show()
########
########
print("乘客的存活情况(饼图)")
plt.subplot(122)
plt.pie([data_not_survived,data_survived],labels=['not_Survived','Survived'],autopct="%1.2f%%")
plt.axis('equal')
plt.legend()
plt.show()
########
########
print("总体性别情况")
data['row.names'].count()
male_number = data[data['sex']=='male']['row.names'].count()
female_number = data[data['sex']=='female']['row.names'].count()

plt.figure(figsize=(10,4),dpi=80)
plt.subplot(121)
sns.countplot(data['sex'])
plt.subplot(122)
plt.pie([male_number,female_number],labels=data['sex'].unique(),autopct='%1.2f%%')
plt.axis('equal')
plt.show()
########存活情况与男女比
########
print("存活下来的男女比")
data_survived = data[data['survived']==1]['row.names'].count()
# 存活数据集
data_survived = data[data['survived']==1]
# 存活数据集中的男性
male_survived_number = data_survived[data_survived['sex']=='male']['sex'].count()

# 存活数据集
data_survived = data[data['survived']==1]
# 存活数据集中的女性
female_survived_number = data_survived[data_survived['sex']=='female']['sex'].count()

plt.figure(figsize=(10,4),dpi=80)
plt.subplot(121)
sns.countplot(x='sex',data=data_survived)
plt.subplot(122)
plt.pie([male_survived_number,female_survived_number],labels=['male','female'],autopct='%1.2f%%')
plt.axis('equal')
plt.legend()
plt.show()
#########存活情况与年龄
#########
print("存活情况与年龄的关系")
print(data['age'].describe())#0.1667-71.0000
data1 = data[data['age'] <= 19]#0.1667-19
data1['row.names'].count()
data1['survived'].sum()
data1_not_survived = data1['row.names'].count() - data1['survived'].sum()
plt.figure(figsize=(10,4),dpi=80)
plt.subplot(121)
sns.countplot(x= 'survived',data = data1)
plt.subplot(122)
plt.pie([data1_not_survived,data1['survived'].sum()],labels=['not survived','survived'], autopct='%1.2f%%')
plt.axis('equal')
plt.legend()
plt.show()

data2 = data[(data['age'] >= 20) & (data['age'] <=39)]#20-39
data2['row.names'].count()
data2['survived'].sum()
data2_not_survived = data2['row.names'].count() - data2['survived'].sum()
plt.figure(figsize=(10,4),dpi=80)
plt.subplot(121)
sns.countplot(x= 'survived',data = data2)
plt.subplot(122)
plt.pie([data2_not_survived,data2['survived'].sum()],labels=['not survived','survived'], autopct='%1.2f%%')
plt.axis('equal')
plt.legend()
plt.show()

data3 = data[(data['age'] >= 40) & (data['age'] <=59)]#40-59
data3['row.names'].count()
data3['survived'].sum()
data3_not_survived = data3['row.names'].count() - data3['survived'].sum()
plt.figure(figsize=(10,4),dpi=80)
plt.subplot(121)
sns.countplot(x= 'survived',data = data3)
plt.subplot(122)
plt.pie([data3_not_survived,data3['survived'].sum()],labels=['not survived','survived'], autopct='%1.2f%%')
plt.axis('equal')
plt.legend()
plt.show()

data4 = data[(data['age'] >= 60) & (data['age'] <=71)]#60-71
data4['row.names'].count()
data4['survived'].sum()
data4_not_survived = data4['row.names'].count() - data4['survived'].sum()
plt.figure(figsize=(10,4),dpi=80)
plt.subplot(121)
sns.countplot(x= 'survived',data = data4)
plt.subplot(122)
plt.pie([data4_not_survived,data4['survived'].sum()],labels=['not survived','survived'], autopct='%1.2f%%')
plt.axis('equal')
plt.legend()
plt.show()
