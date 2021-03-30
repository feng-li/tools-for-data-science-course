def leapyearcheck(year):
    """to judge whether a year is leap year"""
    if year % 100 ==0:
        if year % 400 == 0:
            print(year,'年是闰年')
        else:
            print(year,"年不是闰年")
    elif year % 4 == 0:
        print(year,'年是闰年')
    else:
        print(year,"年不是闰年")
