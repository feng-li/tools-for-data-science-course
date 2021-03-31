year=int(input('输入你要查询的年份：'))
def leapyearcheck(year):
    if year % 4 == 0:
        print(True)
    else:
        print(False)
    return True , False
leapyearcheck(year)
