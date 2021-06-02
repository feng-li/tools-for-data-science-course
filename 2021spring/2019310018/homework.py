# 导入数据分析所需的库、在notebook内可视化数据

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

%matplotlib inline
# 读取预览数据

titanic_df = pd.read_csv('titanic_data.csv')
titanic_df.info()
titanic_df.head()

RangeIndex: 891 entries, 0 to 890
Data columns (total 12 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            714 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Cabin          204 non-null object
Embarked       889 non-null object
dtypes: float64(2), int64(5), object(5)
  
  # 计算缺失数据

titanic_df.isnull().sum()
# 去除Cabin变量

titanic_df = titanic_df.drop('Cabin',axis=1)
# 查看 Embarked 的值的比例

titanic_df.groupby('Embarked').count()

# 对缺失 Embarked 赋值 S 

titanic_df.Embarked[titanic_df.Embarked.isnull()] = ['S']

# 根据平均值、标准差生成随机值

Age_mean = titanic_df['Age'].mean()
Age_std = titanic_df['Age'].std()
Age_null = titanic_df['Age'].isnull().sum()
Age_random = np.random.randint(Age_mean - Age_std, Age_mean + Age_std, size = Age_null)

titanic_df['Age'][np.isnan(titanic_df['Age'])] = Age_random
# 检查整理后的数据

titanic_df.info()
titanic_df.groupby('Embarked').count()
RangeIndex: 891 entries, 0 to 890
Data columns (total 11 columns):
PassengerId    891 non-null int64
Survived       891 non-null int64
Pclass         891 non-null int64
Name           891 non-null object
Sex            891 non-null object
Age            891 non-null float64
SibSp          891 non-null int64
Parch          891 non-null int64
Ticket         891 non-null object
Fare           891 non-null float64
Embarked       891 non-null object
dtypes: float64(2), int64(5), object(4)
  
  # 查看船员遇难和生还情况

titanic_df.Survived.value_counts().plot(kind='pie',autopct='%.2f%%',labels=['Castaway','Survived'])
plt.show()
titanic_df.Survived.value_counts().plot(kind='bar')
plt.xlabel('Castaway0  Survived 1')
plt.ylabel('Passenger')
plt.show()

# 不同级别船票等级Pclass的分布比例
titanic_df.groupby('Pclass')['PassengerId'].count().plot(kind='pie',autopct='%.2f%%')
plt.title('Pclass')
plt.show()

# 不同级别船票等级Pclass的生存和遇难情况
Survived_0 = titanic_df.Pclass[titanic_df.Survived == 0].value_counts()
Survived_1 = titanic_df.Pclass[titanic_df.Survived == 1].value_counts()
pd.DataFrame({'Survived':Survived_1,'Castaway':Survived_0}).plot(kind='bar',stacked='True')
plt.title('Survived Castaway by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Passenger')
plt.show()

# 不同级别船票等级Pclass的幸存概率
titanic_df[['Pclass','Survived']].groupby(['Pclass']).mean().plot(kind='bar')
plt.title('Survived Rate by Pclass')
plt.xlabel('Pclass')
plt.ylabel('Rate')
plt.show()

# 不同性别的乘客生还遇难数据对比
Survived_0 = titanic_df.Sex[titanic_df.Survived == 0].value_counts()
Survived_1 = titanic_df.Sex[titanic_df.Survived == 1].value_counts()
pd.DataFrame({'Survived':Survived_1,'Castaway':Survived_0}).plot(kind='bar',stacked='True')
plt.title('Survived by Sex')
plt.xlabel('Sex')
plt.ylabel('Passenger')
plt.show()

# 不同性别的乘客生还概率
titanic_df[['Sex','Survived']].groupby(['Sex']).mean().plot(kind='bar')
plt.title('Survived Rate by Sex')
plt.xlabel('Sex')
plt.ylabel('Rate')
plt.show()

# 计算船员乘客年龄、幸存遇难者年龄的统计学数据

print titanic_df[['Age']].describe()
print titanic_df[['Age', 'Survived']].groupby(['Survived']).describe()

# 可视化船员乘客年龄分布
plt.figure().add_subplot(1,1,1).hist(titanic_df['Age'],bins=50)
plt.xlabel('Age')
plt.ylabel('passenger')
plt.show()

# 可视化不同年龄段的生还情况
Age_Survived = titanic_df[['Age','Survived']]
Age_Survived['i'] = pd.cut(Age_Survived['Age'], np.arange(0,100,10))
Age_Survived.groupby(['i','Survived'])['Survived'].count().unstack().plot(kind='bar',stacked=True)
plt.xlabel('Age')
plt.ylabel('passenger')
plt.show()

# 可视化不同年龄段生还概率
Age_Survived.drop('Age',axis=1).groupby(['i']).mean().plot(kind='bar')
plt.xlabel('Age')
plt.ylabel('Survived Rate')
plt.show()
