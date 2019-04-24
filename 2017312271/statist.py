import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns  # easy plot

'''x = np.linspace(t.ppf(0.01), #ppf stands for percentiles.
                t.ppf(0.99), 100)
mean, cov = [0, 1], [(1, .5), (.5, 1)]
data = np.random.multivariate_normal(mean, cov, 200)
df = pd.DataFrame(data, columns=["x", "y"])'''

titanic_df = sns.load_dataset("titanic")
print(titanic_df.info())

total_survived_num = titanic_df['survived'].sum()
total_no_survived_num = 891 - total_survived_num
print("生还者 %d 人，%d 人未生还。" % (total_survived_num, total_no_survived_num))

plt.figure(figsize=(10, 5))
plt.subplot(121)
sns.countplot(x='survived', data=titanic_df)
plt.title('Survival count')

plt.subplot(122)
plt.pie([total_no_survived_num, total_survived_num], labels=['No Survived', 'survived'], autopct='%1.0f%%')
plt.title('Survival rate')

plt.show()

plt.figure(figsize=(12, 5))
plt.subplot(121)
titanic_df['age'].hist(bins=70)
plt.xlabel('age')
plt.ylabel('Num')

plt.subplot(122)
titanic_df.boxplot(column='age', showfliers=False)

plt.show()
