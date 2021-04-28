#闰年计算
def leapyearcheck():
	if year % 4 == 0:
		if year % 100 == 0:
			if year % 400 == 0:
				print("是闰年")
			else:
				print("不是闰年")
		else:
			print("是闰年")
	else:
		print("不是闰年")
