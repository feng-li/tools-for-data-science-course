#创建一个月份的字典
month_dict={1:"January",2:"Febrary",3:"March",4:"April",
            5:"May",6:"June",7:"July",8:"August",9:"September",
            10:"October",11:"November",12:"December"}

#构造函数来判断闰年
def isLeapyear(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return True
    else :
        return False


#构造函数来定义月份的天数
def days(year,month):
    if month in (1,3,5,7,8,10,12):
        return 31
    if month in (4,6,9,11):
        return 30
    if month in 2:
        if isLeapyear(year):
            return 29
        else:
            return 28


#构造函数确定时间到1990年1月1日的天数
def getfromtoday(year,month):
    totaldays=0
    for i in range(1990,year):
        if isLeapyear(i):
            totaldays+=366
        else :
            totaldays+=365

    for o in range(1,month):
        totaldays+=days(year,o)
    return totaldays


#判断到该月份有几个星期
def weeks(totaldays):
    Leftdays=totaldays%7
    return Leftdays



#创造构建日历的函数
def canlender(year,month):
    print('\t'+str(year)+"\t"+"\t"+"\t"+month_dict[month])
    print("-------------------------------------------------------------------------")
    print("Mon\tTus\tWed\tThu\tFri\tSat\tSun")
    for p in range (1,weeks(getfromtoday(year,month))+1):
        print("\t",end=" ")
    ii=weeks(getfromtoday(year,month))
    for l in range(1,days(year,month)+1):
        print(l,end="\t")
        ii+=1
        if ii%7==0:
            print(" ")


#引入主函数
def main():
    year=int(input("请输入你的出生年份=   "))
    month=int(input("请输入你的出生月份=    "))
    print(canlender(year,month))
        


main()        
















    
