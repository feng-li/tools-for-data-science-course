
import numpy as np
P = int(input("请输入保费:"))
V = int(input("请输入折现因子:"))
# 折现因子是$v=\frac{1}{1+i}$,其中i是利率
T = int(input("请输入缴纳年限："))
 #T=r-x 缴纳年限的时间是农民工退休的时间减去他参加工作的时间
K = int(input("请输入工资年增长率:"))

Z = []
for t in range(0,int(T)):
    z = P*(1+K)**t*V**t
    Z.append(z)
    print(z)

final_x = np.sum(Z)
print(final_x)




