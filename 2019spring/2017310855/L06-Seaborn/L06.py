#! usr/bin/env python3

import seaborn as sns

# Transfer
data = sns.load_dataset("titanic")

# Logit regress
sns.lmplot(x = "age", y = "survived", hue = "sex", col = "pclass", data = data, logistic = True)
