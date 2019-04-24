
# coding: utf-8

# In[32]:

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import statsmodels.formula.api as smf
from sklearn.cross_validation import train_test_split
from sklearn import metrics
get_ipython().magic('matplotlib inline')


# In[6]:

# Read titanic_data.csv
data = sns.load_dataset("titanic")
data.head()


# In[8]:

# 生存概率
data['survived'].value_counts().plot.pie(autopct='%1.2f%%')
plt.show()


# In[9]:

# 性别与是否存活之间的相关性
sns.factorplot('sex','survived',data = data,size=3,aspect=1.5)
plt.title('Sex and Survived rate')
plt.show()
# 女性的存活率远高于男性


# In[10]:

# 乘客社会等级与是否存活的关系
sns.factorplot('pclass','survived',data=data,size=3,aspect=1.5)
plt.title('Pclass and Survived rate')
plt.show()
# 不同社会等级可能和财富/地位有关系，最后获救的概率可能会不一样；社会等级越高，存活率就越高


# In[12]:

# 配偶及兄弟姐妹的数量与是否存活的关系
sns.factorplot('sibsp','survived',data=data,size=3,aspect=1.5)
plt.title('SibSp and Survived rate')
plt.show()
# 配偶及兄弟姐妹适中的乘客存活率越高


# In[14]:

# 父母与子女的数量与是否存活的关系
sns.factorplot('parch','survived',data=data,size=3,aspect=1.5)
plt.title('Parch and Survived rate')
plt.show()
# 父母与子女数量适中的，存活率更高


# In[64]:

# 基于逻辑回归进行分类预测
Y=data['survived']
X=data.drop(['survived'],axis=1)
feature_selection=list(X.columns);feature_selection # x中包含的变量


# In[65]:

# 删除共线特征
X.drop(['embarked',"who","class","adult_male","deck","embark_town","alive","alone"],axis=1,inplace=True);list(X.columns)


# In[66]:

sex = pd.get_dummies(X["sex"])
# 为防止多重共线性，将哑变量中的Female删除
sex = sex.drop('female', axis = 1);sex
X["sex"] = sex
X.head()


# In[67]:

# 替换缺失值
X.fillna(0);Y.fillna(0);


# In[78]:

X = X.astype("float");Y = Y.astype("float");


# In[79]:

#需要自行添加逻辑回归所需的intercept变量
X['intercept']=1.0
#划分训练集和测试集
X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=1)
X_train.head()
y_train.head()


# In[82]:

#构建逻辑回归分类器
logistic = smf.Logit(y_train,X_train).fit()
logistic.summary()


# In[36]:

#训练误差
predicted=lr.predict(X_train)
#测试误差
y_pred=lr.predict(X_test)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



