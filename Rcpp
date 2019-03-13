---
layout: post
title:  "RCpp 简介"
date:   2018-06-09 16：38：32
categories: R
tags: R
excerpt: 学习RCpp的总结
mathjax: true
---
# Rcpp简介

### 从R到C++

Rcpp 是一个R语言的扩展包.Rcpp提供了一个干净，平易近人的API，可以让你编写**高性能代码.**

C++能加速的典型问题：
+ 多重循环或者递归函数
+ 需要多次调用的函数
+ C++的STL标准模板库中提供多种R中没有的高级数据类型和算法

#### 一个例子！


```R
setwd("D:/Rworkspeace")
library(Rcpp)
sourceCpp("demo1.cpp")

fib_r <- function(n){
  if(n==1||n==2) return(1)
  return(fib_r(n-1)+fib_r(n-2))
}

system.time(fib_r(30))
system.time(fib_cpp(30))
```


       user  system elapsed 
       0.86    0.02    0.88 



       user  system elapsed 
          0       0       0 


### Rcpp安装

+ mac linux用户在R环境install.packages("Rcpp")
+ win用户需要安装[Rtools](https://cran.r-project.org/bin/windows/Rtools/)并添加环境变量,[教程](https://blog.csdn.net/wzgl__wh/article/details/70185687).

### Rcpp常用数据类型

 |类型 |描述 |
 |:-|-|
 |**int/double/bool/String/auto** | 整数型/数值型/布尔值/字符型/自动识别(C++11)|
 |**IntegerVector**  |整型向量|
 |**NumericVector** |数值型向量|
 |**ComplexVector**  |复数向量|
 |**LogicalVector** |逻辑向量|
 |**CharacterVector**|  字符向量|
 |**IntegerMatrix** | 整型矩阵|
 |**NumericMatrix**|数值型矩阵|
 |**LogicalMatrix** | 逻辑矩阵|
 |**CharacterMatrix**| 字符矩阵|
 |**List**  |列表|
 |**DataFrame** | 数据框|


### 常用数据类型初始化

|代码|作用|
|-|-|
|Vector||
| NumericVector V1(n); |创建长度为n的向量V1|
| NumericVector V2=NumericVector::create(1, 2, 3);| 创建向量V2包含三个元素1，2，3|
|Matrix||
| NumericMatrix M1(nrow,ncol);|创建nrow * ncol的数值矩阵|
|List||
|List L=List::create(Named("y1")=y1,Named("y2")=y2);|创建list,名称为y1,y2|
|DataFram||
|DataFrame DF=DataFrame::create(Named("col1")=a,Named("col2")=b,Named("col3")=c);|创建数据框|


### 数据访问

+ Rcpp使用"()"访问元素
+ Cpp中索引从0开始
+ a(0,2)访问矩阵a的第1行第3列

### 常用函数

- +, -, *, /, pow(x,p), <, <=, >, >=, ==, !=, ! 
    + 均支持向量化
- A.size()  
    + 返回向量或矩阵的大小
- A.push_back(a) 
    + 将a添加到A的最后
- A.push_front(a)
    + 将a添加到A的前面
- A.ncol() 
    + 返回A的列数
- A.nrow() 
    + 返回A的行数


### C++函数在R环境运行


```R
scr = "int fib_cpp_1(int n){
         if(n==1||n==2) return 1;
         return(fib_cpp_1(n-1)+fib_cpp_1(n-2));
    }
"
cppFunction(scr)
fib_cpp_1(5)
count<< a<<;
```


5



```R
sourceCpp("demo1.cpp")
fib_cpp(5)
Rcpp::matrix()
```


5


### C++文件的编写规则

#include < Rcpp.h \>    
using namespace Rcpp;     
//[[Rcpp::export]]       

Rcpp::mat funMat(){    
     ...;      
     return mat;    
}
        
            
           
void fun(){    
    ...;          
}



+ 若想在R中使用C++,第一行必须包括在C++文件中
+ 第二行可以不写,但必须使用"Rcpp::"调用Rcpp的类型
+ 第三行必须写在每个想要在R中调用的函数前
+ C++函数和变量必须声明类型
+ C++每行必须以分号结尾
+ 若只对对象本身进行操作可以声明为void型

## RcppArmadillo!!!

Armadillo 是一个非常优秀、现代、高级的C++库,RcppArmadill使得可以在R语言可以基于Rcpp调用Armadillo库.

### 为什么要用RcppArmadillo？

+ RcppArmadillo中有更多的容器
+ RcppArmadillo中对数据操纵更加方便
+ RcppArmadillo中实现了许多Rcpp中没有的常用算法,例如矩阵乘法,转置,求逆,矩阵的常用分解
+ 类似的库还有
    - RInside 在C++中调用R
    - RcppGSL 科学数值计算
    - RcppEigen  线性代数计算库


### RcppArmadillo数据类型与常用函数

RcppAramdillo提供了丰富的数据类型和操作函数,详见[RcppArmadillo帮助文档](http://arma.sourceforge.net/docs.html#part_classes)

### RcppArmadillo文件的编写规则

#include < RcppArmadillo.h \>    
// [[Rcpp::depends(RcppArmadillo)]]    
// [[Rcpp::export]]    

#### 又一个例子！


```R
a=matrix(rnorm(30000),,3)
b=apply(a,1,function(a) sum(a*c(0.3,0.5,0.7))+rnorm(1))
lm(b~a)
```


    
    Call:
    lm(formula = b ~ a)
    
    Coefficients:
    (Intercept)           a1           a2           a3  
       0.006459     0.301525     0.476332     0.716985  
    



```R
sourceCpp("fastlm.cpp")
fastLm(a,b)
```


<dl>
	<dt>$coefficients</dt>
		<dd><table>
<tbody>
	<tr><td>0.3014306</td></tr>
	<tr><td>0.4764750</td></tr>
	<tr><td>0.7169423</td></tr>
</tbody>
</table>
</dd>
	<dt>$stderr</dt>
		<dd><table>
<tbody>
	<tr><td>0.009896280</td></tr>
	<tr><td>0.009824000</td></tr>
	<tr><td>0.009836553</td></tr>
</tbody>
</table>
</dd>
	<dt>$df.residual</dt>
		<dd>9997</dd>
</dl>




```R
library(microbenchmark)
summary(microbenchmark(lm(b~a),fastLm(a,b)))
```


<table>
<thead><tr><th scope=col>expr</th><th scope=col>min</th><th scope=col>lq</th><th scope=col>mean</th><th scope=col>median</th><th scope=col>uq</th><th scope=col>max</th><th scope=col>neval</th></tr></thead>
<tbody>
	<tr><td>lm(b ~ a)   </td><td>7967.553    </td><td>8427.997    </td><td>9054.4853   </td><td>8839.5525   </td><td>9589.329    </td><td>12344.440   </td><td>100         </td></tr>
	<tr><td>fastLm(a, b)</td><td> 238.667    </td><td> 257.778    </td><td> 311.6625   </td><td> 289.7775   </td><td> 314.667    </td><td> 1386.222   </td><td>100         </td></tr>
</tbody>
</table>



### 学习资料

[Advanced R by Hadley Wickham](http://adv-r.had.co.nz/Rcpp.html)    
[Rcpp for everyone](https://teuder.github.io/rcpp4everyone_en/)    
[Rcpp:R与C++的无缝整合](https://item.jd.com/11846729.html)    
[RcppArmadillo](http://arma.sourceforge.net/docs.html#part_classes)    
