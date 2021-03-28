#斐波那契数列

def fb(n):
    a=1
    b=1
    if n<3:
        return a
    else:
        for i in range(0,n-2):
          c=a+b
          a=b
          b=c
        return c

x=int(input("计算的位数："))
print(fb(x))

print("输出1到1000位")
a=1
for i in range(1,1001):
    b=fb(i)
    a=a*b

print(a)
