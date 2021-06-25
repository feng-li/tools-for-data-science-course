1、函数说明
abs(number)返回数字的绝对值，如abs(-10)返回10
pow(x,y[,z])
返回x的y次幂（所得结果对z取模），如pow(2,3)返回8,pow(2,3,3)返回2
cmath.sqrt(number)
返回数字的平方根，数字可以为负数，返回类型为实数，如cmath.sqrt(4)返回2+0j
float(object)
将字符串和数字转换为浮点数，如float(4)返回4.0，float("-1")返回-1.0
math.fabs(number)
返回数字的绝对值，如math.fabs(-10)返回10.0
math.ceil(number)
返回数的上入整数，如math.ceil(4.1)返回5
math.floor(number)
返回数的下舍整数，如math.floor(4.9)返回4

2、常量
常量说明
math.e
返回对数中的e值，math.e返回常量值2.718281828459045
math.pi返回圆周率PI的值，math.pi返回常量值3.141592653589793

3、幂函数和对数函数
函数说明
math.exp(x)
返回e的x次幂,如math.exp(1)返回2.718281828459045
math.log(x[,base])
如math.log(math.e)返回1.0,math.log(100,10)返回2.0
math.log10(x)
返回以10为基数的x的对数，如math.log10(100)返回2.0
math.pow(x,y)返回x的y次幂,如math.pow(2,3)返回8.0
math.sqrt(x)返回x的平方根，不适用于负数，如math.sqrt(9)返回3.0

4、弧度角度转换函数
函数说明
math.degrees(x)将弧度转换为角度,如math.degrees(math.tan(1.0)),返回30.0
math.radians(x)将角度转换为弧度

5、三角函数
函数说明
sin(x)返回正弦值，如math.sin(math.pi/2)返回1.0
cos(x)返回余弦值，如math.cos(math.pi)返回-1.0
tan(x)返回正切值，如math.degrees(math.tan(1.0)),返回30.0
