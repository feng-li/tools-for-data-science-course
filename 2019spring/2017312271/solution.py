import random
import numpy as np
import pandas as pd


def solution():
    a = np.array([random.randint(1, 30) for i in range(10)])
    b = np.array([random.randint(1, 30) for i in range(10)])
    c = np.array([random.randint(1, 30) for i in range(10)])

    delta = (b**2 - 4 * a * c)

    x1 = np.array([])
    slv = pd.DataFrame(columns=['a', 'b', 'c', 'has_root', 'x1', 'x2'])
    slv['a'] = a
    slv['b'] = b
    slv['c'] = c
    slv['has_root'] = delta >= 0

    for i in range(len(slv['has_root'])):
        if slv['has_root'].iloc[i]:
            x1 = (-b[i] + delta[i]**0.5)/(2*a[i])
            x2 = (-b[i] - delta[i]**0.5)/(2*a[i])
            slv['x1'].iloc[i] = x1
            slv['x2'].iloc[i] = x2
            
    return slv

ans = solution()

for i in range(len(ans)):
    row = ans.iloc[i].values # 返回一个list
    print(row)

