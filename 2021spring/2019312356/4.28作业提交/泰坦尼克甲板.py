import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import seaborn as sns

#导入数据：
test_df=pd.read_csv("C:\\Users\\86131\\Downloads\\eval.csv")
train_df=pd.read_csv("C:\\Users\\86131\\Downloads\\train.csv")

# 创建1行1列，大小为10x4 的画布
fig, axes = plt.subplots(nrows=1 ,ncols= 2 ,figsize=(10,4))
 
# 绘制各仓位的幸存率
sns.barplot(x = "deck", y = "survived", data = train_df, ax=axes[0],
            palette="Set2",#调色板
            capsize=0.05,  #横线宽度
            errwidth= 1.2, #误差线宽度
            errcolor="0.1",#误差线颜色透明度，1为白色
            #alpha = 0.8   #透明度
           )
 

 
# 保存图片
fig.savefig("C:\\Users\\86131\\Downloads\\deck.png",dpi = 120)

