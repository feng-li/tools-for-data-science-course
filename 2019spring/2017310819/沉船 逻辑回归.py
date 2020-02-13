import seaborn as sns
import numpy as np
import statsmodels
mytitanic = sns.load_dataset("titanic")
sns.lmplot(x="age", y="survived", data=mytitanic, logistic=True, y_jitter=.03)
