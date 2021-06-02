Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:30:23) [MSC v.1928 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
def leap_year_check(year):
	year = int(input("输入一个年份: "))

if (year % 4) == 0:

   if (year % 100) == 0:

       if (year % 400) == 0:

           print("{0} 是闰年".format(year))   

       else:

           print("{0} 不是闰年".format(year))

   else:

       print("{0} 是闰年".format(year))       

else:

   print("{0} 不是闰年".format(year))