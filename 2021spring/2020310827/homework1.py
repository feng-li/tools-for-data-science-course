year=int(input("Please enter the year:"))
if year % 400 == 0:
    print("yes")
elif yaer % 4 == 0 and year % 100 != 0:
    print("yes")
else:
    print("no")

