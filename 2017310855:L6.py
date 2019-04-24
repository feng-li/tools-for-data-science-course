# 导入sns包
import seaborn as sns
# 调用泰坦尼克数据集
data = sns.load_dataset("titanic")
# logit回归
sns.lmplot(x = "age", y = "survived", hue = "sex", col = "pclass", data = data,logistic = True)