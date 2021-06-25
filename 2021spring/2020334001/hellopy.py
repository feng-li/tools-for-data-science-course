#TDS作业
def leapyearcheck():
    n=input("请输入一个年份：")
    n = int(n)
    
    if n % 400 == 0:
        print(str(n)+"是闰年")
    elif n%4 == 0 and n%100 != 0:
        print(str(n)+"是闰年")
    else:
        print(str(n)+"不是闰年")
    return

leapyearcheck()
