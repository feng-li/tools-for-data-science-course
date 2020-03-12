[(x,y) for x]
[(x,y) for x in [1,2,3] for y in [3,1,4] if x!=y]

def matrixTriIndex(n, diag = True, lower = TRUE):
    return([x, y] for x in range(1, (n+1)) for y in range(1,(n+1)) if y<x)
lowermatrixindex(6)

a = [1,2,3]
b = [4,5,6]
[a[i]+b[i] for i in range(len(a))]

#矩阵
matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
matrix

#矩阵转置
[[row[i] for row in matrix] for i in range(4)]

#元组
t = 12345, 54321, 'hello!'
t[0]
u = t, (1,2,3,4,5)

#字典 有标签
tel = {"Jack": 4098,'Sape':4139}
tel['guido']=4127
print(tel)

sorted(tel.keys())
del tel['Jack']

[x:x**2 for x in (2,4,6,8)]

#集合 相当于字典 没有value
a | b
a^b #一个true一个false

