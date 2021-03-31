def leapyearcheck(n):
    if (n%4)==0:
        if (n%100)==0:
            if (n%400)==0:
                print ('this is a leap year!')
            else:
                print ('this is not a leap year.')
        else:
            print ('this is a leap year!')
    else:
        print ('this is not a leap year.')
