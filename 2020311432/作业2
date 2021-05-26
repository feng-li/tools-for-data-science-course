import numpy as np
 
def fib_matrix(n):
    res = pow((np.mat([[1, 1], [1, 0]])), n) * np.mat([[1], [0]]) #使用mat方法直接定义矩阵
    return res[0][0]
 
for i in range(10):
    print(int(fib_matrix(i)), end=' ')
print('\n')
 
 
### 2
# 使用矩阵计算斐波那契数列
def Fibonacci_Matrix_tool(n):
    Matrix = np.matrix([[1, 1], [1, 0]]) #matrix和mat函数等效
    # 返回是matrix类型
    return pow(Matrix, n)  # pow函数速度快于 使用双星好 **
 
def Fibonacci_Matrix(n):
    result_list = []
    for i in range(0, n):
        result_list.append(np.array(Fibonacci_Matrix_tool(i))[0][0])
    return result_list
 
# 调用
result=Fibonacci_Matrix(10)
for r in result:
    print(r,end=' ')
