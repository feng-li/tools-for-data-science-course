import random
import numpy as np
a = np.random.rand(100000)
a = list(a)
#a中随机取10个
#b1 = random.sample(a,10)
a1 = np.mean(a[1:10000])
a2 = np.mean(a[10001:20000])
a3 = np.mean(a[20001:30000])
a4 = np.mean(a[30001:40000])
a5 = np.mean(a[40001:50000])
a6 = np.mean(a[50001:60000])
a7 = np.mean(a[60001:70000])
a8 = np.mean(a[70001:80000])
a9 = np.mean(a[80001:90000])
a10 = np.mean(a[90001:100000])
lista = [a1,a2,a3,a4,a5,a6,a7,a8,a9,a10]
a_mean = np.mean(lista)
a_all_mean = np.mean(a)
print(a_mean)
print(a_all_mean)
