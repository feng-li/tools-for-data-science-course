i=int(input("请输入一个年份"))
if i%4==0 and i%100!=0 or i%400==0:
    print(i,"是闰年")
else:
    print(i,"不是闰年")

