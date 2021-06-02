year = int(input("输入一个年份: "))

if (year % 4) == 0:

   if (year % 100) == 0:

       if (year % 400) == 0:

           print(year+"是闰年")   

       else:

           print(year+"不是闰年")

   else:

       print(year+"是闰年")     

else:

   print(year+"不是闰年)
