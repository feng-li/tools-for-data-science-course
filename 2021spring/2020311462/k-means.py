import math
import time
import os

total = int(input("请输入要被k-聚类的样本点的总数："))
k0 = int(input("请输入类的总数："))
listi = [i for i in range(0, total)]
listx = []
listy = []
listz = []
for i in range(0, total):
    x = float(input("请输入x[{0}]的值：".format(i)))
    listx.append(x)
    y = float(input("请输入y[{0}]的值：".format(i)))
    listy.append(y)
    z = float(input("请输入z[{0}]的值：".format(i)))
    listz.append(z)
xyz = list(zip(listx, listy, listz))
print("您输入的样本点为：", xyz)

list0 = [[0, 0, 0] for i in range(0, k0)]
listnew = [[] for k in range(0, k0)]
for i in range(0, k0):
    list0[i][0] = listx[i]
    list0[i][1] = listy[i]
    list0[i][2] = listz[i]
print(list0)
avgx, avgy, avgz = [], [], []
for i in range(0, k0):
    avgx.append(list0[i][0])
for i in range(0, k0):
    avgy.append(list0[i][1])
for i in range(0, k0):
    avgz.append(list0[i][2])
distance0 = [0 for i in range(0, k0)]


def distance(which, x, y, z):
    distance0[which] = math.sqrt((avgx[which] - x) ** 2 + (avgy[which] - y) ** 2 + (avgz[which] - z) ** 2)
    return distance0[which]


time0 = time.time()
print(f"正在进行{k0}-均值聚类...")
for t in range(0, total):
    listd = [distance(k, listx[t], listy[t], listz[t]) for k in range(0, k0)]
    for cata in range(0, k0):
        if min(listd) == listd[cata]:
            listnew[cata].append([listx[t], listy[t], listz[t]])
    continue
print(listnew)
avg0 = [[] for k in range(0, k0)]
avgx, avgy, avgz = [], [], []
for k in range(0, k0):
    avgxn = sum([listnew[k][elem][0] for elem in range(0, listnew[k].__len__())]) / listnew[k].__len__()
    avgyn = sum([listnew[k][elem][1] for elem in range(0, listnew[k].__len__())]) / listnew[k].__len__()
    avgzn = sum([listnew[k][elem][2] for elem in range(0, listnew[k].__len__())]) / listnew[k].__len__()
    avgx.append(avgxn)
    avgy.append(avgyn)
    avgz.append(avgzn)
print(avgx, avgy, avgz)

times = 0
while times <= 10:
    times += 1
    listnew = [[] for k in range(0, k0)]
    for t in range(0, total):
        listd = [distance(k, listx[t], listy[t], listz[t]) for k in range(0, k0)]
        for cata in range(0, k0):
            if min(listd) == listd[cata]:
                listnew[cata].append([listx[t], listy[t], listz[t]])
    print(listnew)
    avg0 = [[] for k in range(0, k0)]
    avgx, avgy, avgz = [], [], []
    for k in range(0, k0):
        avgxn = sum([listnew[k][elem][0] for elem in range(0, listnew[k].__len__())]) / listnew[k].__len__()
        avgyn = sum([listnew[k][elem][1] for elem in range(0, listnew[k].__len__())]) / listnew[k].__len__()
        avgzn = sum([listnew[k][elem][2] for elem in range(0, listnew[k].__len__())]) / listnew[k].__len__()
        avgx.append(avgxn)
        avgy.append(avgyn)
        avgz.append(avgzn)
    print(avgx, avgy, avgz)
print(listnew)

time1 = time.time()

print("结论得出")
print("---------------------------final----------------------------")
for i in range(0, k0):
    print(listnew[i], "是第", i, "类")
    print("第", i, "类点中心是", (avgx[i], avgy[i], avgz[i]))

ts = time1 - time0
print(f'共消耗{ts}秒')
