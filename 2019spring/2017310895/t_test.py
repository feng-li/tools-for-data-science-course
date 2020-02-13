from scipy.stats import t
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(t.ppf(0.01,10),t.ppf(0.99,10),10000)
fig,ax=plt.subplots(1,1)
ax.plot(x,t.pdf(x,10),"pink",lw=6,alpha=0.9,label="t pdf")
plt.show()

import seaborn
