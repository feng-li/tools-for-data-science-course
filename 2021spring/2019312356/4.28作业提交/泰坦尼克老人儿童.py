import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

#导入数据：
test_df=pd.read_csv("C:\\Users\\86131\\Downloads\\eval.csv")
train_df=pd.read_csv("C:\\Users\\86131\\Downloads\\train.csv")

# 创建1行2列，大小为10x4 的画布
fig, axes = plt.subplots(nrows=1 ,ncols= 2 ,figsize=(10,4))
 
# 选取数据 
children = train_df[train_df["age"]<=14]
elder= train_df[train_df["age"]>=60]
 
# 绘制儿童幸存与否直方图
ax = sns.histplot(children[children["survived"]==1].age.dropna(), 
                  color="green",#可以自定义颜色
                  bins=18, label = "survived", ax = axes[0], kde =False)
 
ax = sns.histplot(children[children["survived"]==0].age.dropna(),
                  color="red",
                  bins=40, label = "Not_survived", ax = axes[0], kde =False)
 
# 添加图例和标题
ax.legend()
ax.set_title("Children")
 
 
# 在画布第2列绘制老人幸存与否直方图
_ax = sns.histplot(elder[elder["survived"]==1].age.dropna(), 
                  color="green",
                  bins=18, label = "Survived", ax = axes[1], kde =False)
 
_ax = sns.histplot(elder[elder["survived"]==0].age.dropna(),
                   color="red",
                  bins=40, label = "Not_survived", ax = axes[1], kde =False)
# 添加图例和标题
_ax.legend()
_ax.set_title("Elder")
 
# 保存图片
fig.savefig("C:\\Users\\86131\\Downloads\\child_and_elder.png",dpi = 120)

