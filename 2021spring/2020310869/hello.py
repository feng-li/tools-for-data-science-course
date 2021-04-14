import math
print(5+1)
print(6-1)
print(5*2)
print(5/2)
print(math.sin(5))
def leap_year_check():
	year = input()
	year=int(year)
	if year%4 ==0:
		print('yes')
	else:
		print('no')

leap_year_check()