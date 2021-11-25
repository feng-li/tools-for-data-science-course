import math
n = int(input("请输入想查询的项数："))

def Fi_Sequence(n):
    m = math.sqrt(5)
    result = 1/m*(((1+m)/2)**n - ((1-m)/2)**n)
    return result

Fi_Sequence(n)
i = 1
i_sum = Fi_Sequence(i)
for i in range(1,1001):
    calculate = i_sum * Fi_Sequence(i+1)
    i += 2
    if i == 1000:
        print(calculate)
