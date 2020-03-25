#输出一个直角三角形形状的数字
def triangles(n):
    L=[1]
    for x in range(n):
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
for x in triangles(10):
    print(x)
