{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math\n",
    "math.exp(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import math as mt\n",
    "mt.exp(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "1.0"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import exp\n",
    "exp(0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [3, 4]])"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "A = np.array([[1,2],[3,4]])\n",
    "A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 3],\n",
       "       [2, 4]])"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.T  #求矩阵的转置"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2, 3],\n",
       "       [4, 5, 6],\n",
       "       [7, 8, 9]])"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A = np.array([[1,2,3],[4,5,6],[7,8,9]])\n",
    "A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 4, 7],\n",
       "       [2, 5, 8],\n",
       "       [3, 6, 9]])"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.T \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 3.15251974e+15, -6.30503948e+15,  3.15251974e+15],\n",
       "       [-6.30503948e+15,  1.26100790e+16, -6.30503948e+15],\n",
       "       [ 3.15251974e+15, -6.30503948e+15,  3.15251974e+15]])"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Scipy（Scientific Python）:可以利用numpy做更高级的数学，信号处理，优化，统计等\n",
    "from scipy import linalg\n",
    "B = linalg.inv(A) # 求矩阵的逆\n",
    "B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1, 2],\n",
       "       [3, 4]])"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import numpy as np\n",
    "A = np.array([[1,2],[3,4]])\n",
    "A"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-2. ,  1. ],\n",
       "       [ 1.5, -0.5]])"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Scipy（Scientific Python）:可以利用numpy做更高级的数学，信号处理，优化，统计等\n",
    "from scipy import linalg\n",
    "B = linalg.inv(A) # 求矩阵的逆\n",
    "B"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[1.0000000e+00, 0.0000000e+00],\n",
       "       [8.8817842e-16, 1.0000000e+00]])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "A.dot(B)#矩阵乘法"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x20b7ec7b388>]"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#matplotlib  一个python 的2D 绘图库\n",
    "%matplotlib inline\n",
    "import matplotlib.pyplot as plt\n",
    "x= [1,2,3,4,5,6]\n",
    "y= [3,4,6,2,4,8]\n",
    "plt.plot(x,y)\n",
    "##########################如果不显示图，有两种解决办法\n",
    "#1.在import 之前，先加入  %matplotlib inline \n",
    "#2.或者在最后面加plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "def parity(n):\n",
    "    \"\"\"To judge whether an integer is odd or even\"\"\"  #the function help\n",
    "    if n % 2 == 0:\n",
    "        print(n,'is odd',sep='')\n",
    "    elif n % 2 == 1 :\n",
    "        print(n,'not odd',sep='')\n",
    "    else:\n",
    "        print(n,'neither odd nor ',sep='')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on function parity in module __main__:\n",
      "\n",
      "parity(n)\n",
      "    To judge whether an integer is odd or even\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(parity)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3not odd\n"
     ]
    }
   ],
   "source": [
    "parity(3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "10000"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#匿名函数，关键字lambda表示匿名函数\n",
    "#冒号前面的  x 表示函数参数，后面只能有一个表达式，不用写return，返回值就是该表达式的结果\n",
    "f= lambda x : x ** 2\n",
    "f(100)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "def make_incrementor(n):\n",
    "    return lambda x:x+n  #返回一个函数"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "f = make_incrementor(42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(42, 43)"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "f(0),f(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [],
   "source": [
    "#汉诺塔问题：定义一个函数，接收参数n\n",
    "#表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法\n",
    "def move(n,a,b,c):\n",
    "    if n ==1 :\n",
    "        print(a,'-->',c)\n",
    "    else:\n",
    "        move(n-1,a,c,b)\n",
    "        move(1,a,b,c)\n",
    "        move(n-1,b,a,c)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "A --> C\n",
      "A --> B\n",
      "C --> B\n",
      "A --> C\n",
      "B --> A\n",
      "B --> C\n",
      "A --> C\n"
     ]
    }
   ],
   "source": [
    "move(3,'A','B','C')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "某些函数定义时设置了多个参数，使用默认参数可以简化该函数的调用"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [],
   "source": [
    "def power(x,n=2):\n",
    "    s=1\n",
    "    while n > 0 :\n",
    "        s=s*x\n",
    "        n=n-1\n",
    "    return s"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "25"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "power(5)#只输入一个数，默认求平方"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "125"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "power(5,3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "80"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import functools\n",
    "int2=functools.partial(int,base=2)\n",
    "int2('1010000')  #相当于int('1000000',base=2) ,即默认二进制转换为十进制"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [],
   "source": [
    "def triangles(n):  #杨辉三角\n",
    "    L =[1]\n",
    "    for x in range(n):\n",
    "        yield L\n",
    "        L =[1]+[L[i]+L[i+1] for i in range(len(L)-1)] + [1]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "[1, 1]\n",
      "[1, 2, 1]\n",
      "[1, 3, 3, 1]\n",
      "[1, 4, 6, 4, 1]\n",
      "[1, 5, 10, 10, 5, 1]\n",
      "[1, 6, 15, 20, 15, 6, 1]\n",
      "[1, 7, 21, 35, 35, 21, 7, 1]\n",
      "[1, 8, 28, 56, 70, 56, 28, 8, 1]\n",
      "[1, 9, 36, 84, 126, 126, 84, 36, 9, 1]\n"
     ]
    }
   ],
   "source": [
    "for x in triangles(10):\n",
    "    print((x))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'C:\\\\Users\\\\Asus'"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pwd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
