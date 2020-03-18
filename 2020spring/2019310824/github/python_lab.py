import random
operator=random.choice('+-*/')#在输入的几个字符串中任选一个，但其实是str形式
num1=random.randrange(10)#从一到十输入随机整数
num2=random.randrange(10)
if operator=='+':
    result=num1+num2
elif operator=='-':
    result=num1-num2
elif operator=='/':
    result=num1//num2
else :
     result=num1*num2
while True:  #input中只能接受一个对象，+连接的算一个，‘，’连接的算多个
    user_result=int(input(str(num1)+operator+str(num2)+'='))
    if user_result==result:
        print('Correct!')
        break
    else:
          print('Wrong!Try again!')
