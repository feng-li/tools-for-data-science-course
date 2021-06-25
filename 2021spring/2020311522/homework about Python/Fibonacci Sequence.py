import math
n = int(input("请输入想查询的项数："))

def Fi_Sequence():
    m = math.sqrt(5)
    result = 1/m*(((1+m)/2)**n - ((1-m)/2)**n)
    return result

Fi_Sequence()
Fi = Fi_Sequence()
print(Fi)
