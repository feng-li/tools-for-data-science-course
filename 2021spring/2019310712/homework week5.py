year = int(input("请输入年份:"))
if year % 4 == 0 and year % 400 == 0:
    print("闰年")
elif year % 4 == 0 and year % 100 != 0:
    print("闰年")
else:
    print("平年")
