#判断是否为闰年
year = input("请您输入一个年份:")
if int(year) % 4 == 0:
	print("你输入的是一个闰年")
else:
	print("你输入的不是一个闰年")
