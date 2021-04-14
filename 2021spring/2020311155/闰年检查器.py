# -*- coding = utf-8 -*-
# @Time :2021/3/24 9:02 pm
# @Author : Lily
# @File :闰年检查器.py
# @Mac :PyCharm
i=0
while i<999:
    def YearCheck():
        '''to judge whether the year is leap year'''
    year=int(input('请输入一个年份'))
    if year%4==0 and year%100!=0 or year%400==0:
        print(year,'是闰年')
    else:
        print(year,'不是闰年')



