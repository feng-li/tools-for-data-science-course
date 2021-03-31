ear = input("请输入您要判断的年份：")
year = int(year)
result = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
if result:
    s = "是"
else:
    s = "不是"
print("{0}年{1}闰年".format(year, s))
————————————————
版权声明：本文为CSDN博主「m0_38056893」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/m0_38056893/article/details/79683732
