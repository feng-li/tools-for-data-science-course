import seaborn as sns
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
data = sns.load_dataset('titanic')
data = pd.DataFrame(data)
data.replace("male",1,inplace=True)
data.replace("female",0,inplace=True)
varsata = data.replace(to_replace="?", value=np.NaN)
data = data.dropna()
sns.lmplot(x="age",y="survived",data=data,hue="sex",
           markers=["x","o"],palette="Set1",logistic=True)
X=data[["sex","age"]]
y=data["survived"]
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=22)
esmitor=LogisticRegression()
esmitor.fit(X_train,y_train)
esmitor.score(X_test,y_test)
