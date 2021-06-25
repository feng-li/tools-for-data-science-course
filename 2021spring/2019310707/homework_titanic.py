import numpy as np
import pandas as pd
a=open(r'C:\Users\18516\Desktop\titanic-data.csv')
b=open(r'C:\Users\18516\Desktop\titanic-data.csv')
train=pd.read_csv(a)
test=pd.read_csv(b)
print('训练数据集',train.shape,'测试数据集',test.shape)

full=train.append(test,ignore_index=True)
full.head()
full.info()

full['Age']=full['Age'].fillna(full['Age'].mean())
full['Fare']=full['Fare'].fillna(full['Fare'].mean())
full['Embarked'].value_counts()
full['Embarked']=full['Embarked'].fillna('S')
full['Cabin']=full['Cabin'].fillna('U')
full.info()

sex_mapDict={'male':1,'female':0}
sex=full['Sex'].map(sex_mapDict)
sex.head()

embarkedDf=pd.DataFrame()
embarkedDf=pd.get_dummies(full['Embarked'],prefix='Embarked')
embarkedDf.head()

full=pd.concat([full,embarkedDf],axis=1)
full.drop('Embarked',axis=1,inplace=True)
full.head()

pclassDf=pd.DataFrame()
pclassDf=pd.get_dummies(full['Pclass'],prefix='Pclass')
full=pd.concat([full,pclassDf],axis=1)
full.drop('Pclass',axis=1,inplace=True)
full.head()

full['Name'].head()
def getTitle(name):
    name=str(name)
    str1=name.split(',')[1]
    str2=str1.split('.')[0]
    str3=str2.strip()
    return str3
titleDf=pd.DataFrame()
titleDf['Title']=full['Name'].map(getTitle)
titleDf.head()
title_mapDict = {
                    "Capt":       "Officer",
                    "Col":        "Officer",
                    "Major":      "Officer",
                    "Jonkheer":   "Royalty",
                    "Don":        "Royalty",
                    "Sir" :       "Royalty",
                    "Dr":         "Officer",
                    "Rev":        "Officer",
                    "the Countess":"Royalty",
                    "Dona":       "Royalty",
                    "Mme":        "Mrs",
                    "Mlle":       "Miss",
                    "Ms":         "Mrs",
                    "Mr" :        "Mr",
                    "Mrs" :       "Mrs",
                    "Miss" :      "Miss",
                    "Master" :    "Master",
                    "Lady" :      "Royalty"
                    }
titleDf['Title'] = titleDf['Title'].map(title_mapDict)
titleDf=pd.get_dummies(titleDf['Title'])
titleDf.head()
full=pd.concat([full,titleDf],axis=1)
full.drop('Name',axis=1,inplace=True)
full.head()

cabinDf=pd.DataFrame()
full['Cabin']=full['Cabin'].map(lambda c: c[0])
cabinDf=pd.get_dummies(full['Cabin'],prefix='Cabin')
full = pd.concat([full,cabinDf],axis=1)
full.drop('Cabin',axis=1,inplace=True)
full.head()

familyDf=pd.DataFrame()
familyDf['FamilySize']=full['Parch']+full['SibSp']+1
familyDf['Family_Single']=familyDf['FamilySize'].map(lambda s:1 if s==1 else 0)
familyDf['Family_Small']=familyDf['FamilySize'].map(lambda s:1 if 2<=s<=4 else 0)
familyDf['Family_Large']=familyDf['FamilySize'].map(lambda s:1 if s>=5 else 0)
familyDf.head()

full = pd.concat([full,familyDf],axis=1)
full.head()

corrDf=full.corr()
corrDf
corrDf['Survived'].sort_values(ascending=False)

full_X = pd.concat( [titleDf,#头衔
                     pclassDf,#客舱等级
                     familyDf,#家庭大小
                     full['Fare'],#船票价格
                     cabinDf,#船舱号
                     embarkedDf,#登船港口
                     full['Sex']#性别
                    ] , axis=1 )
full_X.shape


sourceRow=891
source_X=full_X.loc[0:sourceRow-1,:]
source_y=full_X.loc[0:sourceRow-1,:]
pred_X=full_X.loc[sourceRow:,:]
from sklearn.cross_validation import train_test_split
train_X,test_X,train_y,test_y=train_test_split(source_X,source_y,train_size=0.8)
print('原始数据特征',source_X.shape,'训练数据特征',train_X.shape,'测试数据特征',test_y.shape)
print('原始数据标签',source_X.shape,'训练数据标签',train_X.shape,'测试数据标签',test_y.shape)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit( train_X , train_y )
model.score(test_X , test_y )

"""
Spyder Editor

This is a temporary script file.
"""

