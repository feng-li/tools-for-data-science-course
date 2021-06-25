import pandas as pd
import matplotlib.pyplot as plt
 
train = pd.read_csv('train.csv')
 
#print(train.info())

train['Age']=train['Age'].fillna(train['Age'].mean())
 
Pclass_1=train[train['Pclass']==1].mean()['Age']
Pclass_2=train[train['Pclass']==2].mean()['Age']
Pclass_3=train[train['Pclass']==3].mean()['Age']
rects=plt.bar(['1','2','3'],[Pclass_1,Pclass_2,Pclass_3])
plt.xlabel("Pclass")
plt.ylabel("averageAge")
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(round(height,2)), ha='center', va='bottom')
plt.show()
 
Total=len(train['Pclass'])
Survived_1=train[train['Pclass']==1]['Survived'].sum()
Survived_2=train[train['Pclass']==2]['Survived'].sum()
Survived_3=train[train['Pclass']==3]['Survived'].sum()
rects=plt.bar(['1','2','3'],[Survived_1/Total,Survived_2/Total,Survived_3/Total])
plt.xlabel("Pclass")
plt.ylabel("survivalRate")
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(round(height*100,2))+'%', ha='center', va='bottom')
plt.show()
 
Total=len(train['Sex'])
Survived_male=train[train['Sex']=='male']['Survived'].sum()
Survived_female=train[train['Sex']=='female']['Survived'].sum()
rects=plt.bar(['male','female'],[Survived_male/Total,Survived_female/Total])
plt.xlabel("Sex")
plt.ylabel("survivalRate")
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(round(height*100,2))+'%', ha='center', va='bottom')
 
plt.show()
 
Pclass_1=train[train['Pclass']==1]

Pclass_1_male=Pclass_1[Pclass_1['Sex']=='male']['Survived'].sum()

Pclass_1_female=Pclass_1[Pclass_1['Sex']=='female']['Survived'].sum()
 
Pclass_2=train[train['Pclass']==2]

Pclass_2_male=Pclass_2[Pclass_2['Sex']=='male']['Survived'].sum()

Pclass_2_female=Pclass_2[Pclass_2['Sex']=='female']['Survived'].sum()
 
Pclass_3=train[train['Pclass']==3]

Pclass_3_male=Pclass_3[Pclass_3['Sex']=='male']['Survived'].sum()

Pclass_3_female=Pclass_3[Pclass_3['Sex']=='female']['Survived'].sum()
 
rects=plt.bar(['1_male','1_female','2_male','2_female','3_male','3_female'],
        [Pclass_1_male/Total,Pclass_1_female/Total,
         Pclass_2_male / Total, Pclass_2_female / Total,
         Pclass_3_male / Total, Pclass_3_female / Total])
plt.xlabel("PclassAndSex")
plt.ylabel("survivalRate")
for rect in rects:
    height = rect.get_height()
    plt.text(rect.get_x() + rect.get_width() / 2, height, str(round(height*100,2))+'%', ha='center', va='bottom')
 
plt.show()
