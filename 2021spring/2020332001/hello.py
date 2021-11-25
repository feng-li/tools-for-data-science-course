def jisuanqi():   
 #实现加减乘除运算
    a, b, c=shuru()
    if c == "+":
        z = a + b
        print("%s+%s 的和为%s"%(a, b, z))
    elif c == "-":
        z = a - b
        print("%s-%s 的差为%s" % (a, b, z))
    elif c == "*":
        z = a * b
        print("%s*%s 的积为%s" % (a, b, z))
    elif c == "/":
        z = a / b
        print("%s/%s 的商为%s" % (a, b, z))
    else:
        print("error operate")

def shuru():
    #int是强转为整数型 str为了强转为字符串
    a= int(input("输入数字1："))
    b= int(input("输入数字2："))
    operate= str(input("输入运算法则："))
    return a,b,operate

while 1:
    #让计算器可以循环使用
    p=input("请输入p的值：")
    if p == 'y':
        jisuanqi()
    else:
        break
