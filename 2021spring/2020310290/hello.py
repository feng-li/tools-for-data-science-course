def number(n):
    a=[1,1]
    for x in range(0,n-2):
        c=a[x]+a[x+1]
        a.append(c)
    return a
def multiply(l):
    o=1
    for i in range (0,len(l)):
        o=o*l[i]
    print(o)
def inply(m):
    for i in range(0,m/2):
        if 2**i<m and 2**(i+1)>m :
            b=i
            return b
    for i in range (0,m/3):
        if 3**i<m-2**b and 3**(i+1)>m-2**b :
            v=i
            return v
    print("大体数字是="+"2**"+str(b)+"+"+"3**"+str(v)+"+"+str(m-2**b-3**v))
    
m=6
n=number(m)
k=multiply(n)
inply(k)

