ear = input("请输入您要判断的年份：")
year = int(year)
result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if result:
    s = "是"
else:
    s = "不是"
print("{0}年{1}闰年".format(year, s))
