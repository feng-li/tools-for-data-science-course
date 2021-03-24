print("hello world")
num1 = 10
num2 = 15
#下面测试基本运算
add = num1 + num2
subtract = num1 - num2
multiply = num1 * num2
division = num1 / num2
mod = num2 % num1
power = pow(num1, 2)
power_02 = num1 ** 2


#逻辑运算
re1 = num1 > num2

def Fibonacci(n):
  ls = [1, 1]
  if n == 1 or n == 2:
    return ls[n]
  for i in range(3, n+1):
    ls[0], ls[1] = ls[1], ls[0]+ls[1]
   return ls[1]
