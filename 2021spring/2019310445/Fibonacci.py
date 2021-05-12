#创建一个输出为斐波那契数列的函数，其中n为项数
def creFibNum(n):#n 为要输出的斐波那契数列个数
    Fib=[0,1]
    for i in range (n-1):
        Fib.append(Fib[-2]+Fib[-1])
    return Fib[1:]

#创建一个输出为斐波那契数列的函数，其中n为允许的最大上限
def creFibMax(n):
    Fib=[0,1]
    while 1:# 无穷循环
         if Fib[-1]>n:
            break 
         Fib.append(Fib[-2]+Fib[-1])#循环结束时一定包括一个大于n的数
    Fib.pop() #应该有更好的办法来解决这个问题      
    return Fib[1:]

#test=creFibMax(10)
#for i in range(len(test)) :
#    print(test[i])

#按位运算
def calMulti(n): #n是小于的指标
    MAX=100 #位运算能储存的位数
    a=[0]*MAX #位运算数组
    a[0]=1  #从1开始乘，这是斐波那契数列的第一项
    d=1 #从第一位开始计算
    fib=creFibMax(n)
    for i in fib: #外层循环，
        num=0
        for j in range(0,d): #d是不被包含在内的。第一次，d=1，算一次
            temp=a[j]*i+num #将每一个数的每一位数都乘上i
            a[j]=temp%10 #将每一个数的每一位数利用数组存储，取余数
            num=temp//10 #整除，保留更高位的数

        while num: #判断对已经有的位数d做完运算后，是否需要进位
            a[d]=num%10
            num=num//10
            d+=1

    for i in range(d-1,-1,-1): #倒序输出
        print(a[i],end="") # 不换行
    print()
    return 0
num=int(input("Please enter a positive integer as the maximum of a Fibonacci sequence:"))
print("The product of the Fibonacci sequence less than",num,"is")
calMulti(num)
