def leapyearcheck(n):
    if (n%4)==0:
        if (n%100)==0:
            if (n%400)==0:
                print ('是闰年')
            else:
                print ('不是闰年')
        else:
            print ('是闰年')
    else:
        print ('不是闰年')
