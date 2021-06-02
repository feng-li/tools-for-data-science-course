# -*- coding = utf-8 -*-
# 作者：汪成智
# 学号：2020311476
# 创建时间：2021/3/28 22:35
# 开发环境：PyCharm

year=int(input("pls enter the year:"))

if year%100 != 0:
    if year%4 == 0:
        print(year,"is a leap year.")
    else:
        print(year,"is not a leap year.")
else:
    if year%400 == 0:
        print(year,"is a leap year.")
    else:
        print(year, "is not a leap year.")

print("the program is over!")