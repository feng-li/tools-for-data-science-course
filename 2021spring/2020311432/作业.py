#读取数据
import  pandas as pd
data = pd.read_csv(r"C:\Users\lhf\PycharmProjects\python+MachineLeaning\泰坦尼克号数据\data.csv")
#处理数据
#1.筛选特征  名字不重要，Cabin缺太多，票号不重要
data.drop(["Name","Cabin","Ticket"],inplace= True,axis=1)#将要删除的那一列的名字放到列表中，inplace=True表示生成的新的数据代替旧的数据,axis=1 删除列

#2.处理缺失值  Age缺很多数据，
data["Age"] = data["Age"].fillna(data["Age"].mean())  #用年龄的平均值填补缺失值   注意是方括号！！！
   #Embarked 缺两个数据 ,把缺的两行删除
data = data.dropna()#删除有缺失值的行  默认是axis = 0

#3.数据中出现非数字的数据，将它转换成数字，有两种方法
#3.1 第一种方法
label = data["Embarked"].unique().tolist()  #取出Embarked中所有的取值并转化成列表------类似于集合形式
data["Embarked"] = data["Embarked"].apply(lambda x:label.index(x))
#3.2 第二种方法
data["Sex"] = (data["Sex"] == "male").astype("int") #将男人=1，女人=0

#4.分离特征和标签
x = data.iloc[:,data.columns != "Survived"]  #取出data数据中列名不为"Survived"的其他列
y = data.iloc[:,data.columns == "Survived"]  #取出data数据中列名为"Survived"的列

#训练集，测试集划分
from sklearn.model_selection import train_test_split
Xtrain,Xtest,Ytrain,Ytest = train_test_split(x,y,test_size=0.3) #划分后数据索引会变混乱 Xtrain,Xtest把x分了7：3，Ytrain,Ytest把y分了7：3
for i in [Xtrain,Xtest,Ytrain,Ytest]:
    i.index = range(i.shape[0])   #将索引改成0-621
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
#网格搜索 能帮助我们同时调整多个参数的技术 枚举技术
parameters = {"criterion":("gini","entropy")
              ,"splitter":("best","random")
              ,"max_depth":list(range(1,10))
              ,"min_samples_leaf":list(range(1,50,5))
              ,"min_impurity_decrease":list(np.linspace(0,0.5,20))}
clf = DecisionTreeClassifier(random_state= 25)
GS = GridSearchCV(clf,parameters,cv=10) #GridSearchCV同时满足了fit，score，cross_val_score
GS = GS.fit(Xtrain,Ytrain)
print(GS.best_params_) #从我们输入的参数和参数列表中，返回最佳组合   最佳参数组合
print(GS.best_score_)#网格搜索后的模型的评价标准
