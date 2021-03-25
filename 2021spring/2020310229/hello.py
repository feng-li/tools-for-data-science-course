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
    ls = [1,1]
    if n ==1 and n ==2:
        return ls[0]
    for i in range(3,n+1):
        ls[0], ls[1] = ls[1], ls[0]+ls[1]
    return ls[1]
"""while True:
    a = input("input a number")
    a = int(a)
    print(Fibonacci(a))
"""

def multi_within_ten(a,b):
    aa = list(str(a))[::-1]
    len_a = len(str(a))
    next = 0
    result = []
    for i in range(len_a):
        curr = int(aa[i]) * b + next
        len_curr = len(str(curr))
        if len_curr >= 2:
            curr_list = list(str(curr))[::-1]
            next = int(curr_list[1])
            this = curr_list[0]
        else:
            next = 0
            this = curr
        result.append(int(this))

    if next != 0:
        result.append(next)

    return result


def add_(a, b):
    len_a = len(a)
    len_b = len(b)
    next = 0
    result = []
    if len_a < len_b:
        a = a + [0 for i in range(len(b) - len(a))]
        a = a
    elif len_a > len_b:
        b = b + [0 for i in range(len(a) - len(b))]
        b = b

    for i in range(max(len_a, len_b)):
        curr = a[i] + b[i] + next
        if len(str(curr)) >= 2:
            curr_list = list(str(curr))
            this = int(curr_list[1])
            next = int(curr_list[0])
        else:
            this = curr
            next = 0
        result.append(this)
    if next != 0:
        result.append(next)
    return result


def mutli_over_ten(a, b):
    list_b_0 = list(str(b))[::-1]
    list_b = [int(i) for i in list_b_0]
    len_b = len(str(b))
    result = []

    count = 0
    for i in range(len_b):

        curr_result = multi_within_ten(a ,list_b[i])
        curr_result = curr_result[::-1] + [0]*count
        curr_result = curr_result[::-1]
        result.append(curr_result)
        count += 1

    for i in range(1, len(result)):
        result[i] = add_(result[i-1], result[i])


    #这里将列表转换成数字
    result_str_list = [str(i) for i in result[-1]][::-1]
    result_str = "".join(result_str_list)
    result_num = int(result_str)
    return result_num


def main(n):
    result = 1
    for i in range(1, n+1):
        fabonacci = Fibonacci(i)
        result = mutli_over_ten(result, fabonacci)
    return result



# 100为参数，可以任意修改。但是本算法效率比较低
#下面的函数打印的是前斐波那契数列前100个的乘积
print(main(100))
