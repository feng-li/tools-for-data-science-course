ys=int(input("请输入要查询的年份："))
term1=(ys%4==0 and ys%100!=0)
term2=(ys%400==0)
if(term1 or term2):
    print("恭喜：",ys,"是闰年！")
else:
    print("抱歉，不是！")
