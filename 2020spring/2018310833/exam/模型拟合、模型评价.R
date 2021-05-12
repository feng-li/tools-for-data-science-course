rm(list = ls())

##导入数据
library(readxl)

##在6000+个数据中抽取1000个
data0 = read_excel("C:/Users/Jellysillyfish/Desktop/diamonds筛选+替换.csv")
set.seed(123)
diamonds <- data0[sample(1:6689,2000),]
id <- sample(1:2000,2000/2)
a <- diamonds[id,]
Y=a[,7]
X=t(t(a[,c(1:6)]))
n = 1000
p = 6

##进行数据标准化


#响应变量
a$price = scale(a$price,center = FALSE,scale = TRUE)
#预报变量
a$carat = scale(a$carat,center = FALSE,scale = TRUE)
a$cut = scale(a$cut,center = FALSE,scale = TRUE)
a$color = scale(a$color,center = FALSE,scale = TRUE)
a$clarity = scale(a$clarity,center = FALSE,scale = TRUE)
a$depth = scale(a$depth,center = FALSE,scale = TRUE)
a$table = scale(a$table,center = FALSE,scale = TRUE)

par(mfrow = c(2,3))
##用carat做回归分析
lm0 <- lm(price ~ carat,data = a)
summary(lm0)

##用其余变量进行回归
lm1 <- lm(price ~ carat + I(carat^2) + I(carat^3)+cut+color+clarity+depth+table,data = a)
summary(lm1)
plot(lm1)

## 二维图（图矩阵）
cor(a[,1:7])
pairs(a[,1:7])

##方差分析表
anova(lm1)
##残差数据
e=residuals(lm1)   ###残差
Yhat=fitted(lm1)
Leverge=influence(lm1)$hat
##hatvalues(lm1)
##hat(X)

#sigma_hat
sigma=summary(lm1)$sigma
#标准化残差
r=(e/sigma)*(1/sqrt(1-Leverge))
##r=rstandard(lm1)
sigma_i=influence(lm1)$sigma
r_i=e*(1/sigma_i)*(1/sqrt(1-Leverge))
X1 = a$carat
X2 = a$cut
X3 = a$color
X4 = a$clarity
X5 = a$depth
X6 = a$table
##标准化残差对自变量散点图
par(mfrow=c(2,3))
plot(X1,r)             ###第一幅图有异方差的情况，推断是价格与克拉数之间为几何倍增长的关系。
plot(X2,r)
plot(X3,r)
plot(X4,r)
plot(X5,r)
plot(X6,r)

##标准化残差顺序图##
plot(r)
##异常点、高杠杆点、强影响点

e=residuals(lm1)
Leverge=influence(lm1)$hat
##hatvalues(lm1)
##hat(X)
r=rstandard(lm1)
## 异常点识别：标准化残差绝对值大于2或3
pos1=which(abs(r)>2)
pos1
pos2=which(abs(r)>3)
pos2
## 高杠杆点识别：杠杆值大于 2*(p+1)/n
pos3=which(Leverge>2*(p+1)/n)
pos3


## 4.9 观测影响度量
par(mfrow=c(2,2))
sigma_i=influence(lm1)$sigma
##r_i=e*(1/sigma_i)*(1/sqrt(1-hat))
r_i=rstudent(lm1)

## Cook 距离
C=cooks.distance(lm1)
sigma=summary(lm1)$sigma
C1=colSums((cbind(rep(1,n),X)%*%t(influence(lm1)$coefficients))^2)/(sigma^2*(p+1))
C2=(r^2/(p+1))*(Leverge/(1-Leverge))
C[1:10]
C1[1:10]
C2[1:10]
plot(C,ylab="Cook")

## Welsch and Kuh 度量
DFITS=dffits(lm1)
DFITS1=diag(cbind(rep(1,n),X)%*%t(influence(lm1)$coefficients))*(1/sigma_i)*(1/Leverge^(0.5))
DFITS2=r_i*sqrt(Leverge/(1-Leverge))
DFITS[1:10]
DFITS1[1:10]
DFITS2[1:10]
plot(abs(DFITS),ylab="|DFITS|")

#### 强影响点识别
pos4=which(abs(DFITS)>2*sqrt((p+1)/(n-p-1)))
pos4


## Hadi度量
d_square=(e/sqrt(sum(e^2)))^2
H=(Leverge/(1-Leverge))+(p+1)*(1/(1-Leverge))*(d_square/(1-d_square))

plot(H,ylab="Hadi")


## 4.10 位势-残差图
pot=Leverge/(1-Leverge)
res=(p+1)*(1/(1-Leverge))*(d_square/(1-d_square))
plot(res,pot,xlab="Residual",ylab="Potential")

##证明受到carat变量影响较大，
##图形表明钻石的克拉数与价格之间的关系不是直线关系
##我们也许可以用含一个弯曲的曲线来提高预测精度

##因此c从头进行多项式回归分析
library(ggplot2)
set.seed(1234)
d <- read.csv("C:/Users/user/Desktop/diamonds1.csv")
diamonds <- d[sample(1:6689,2000),]
id <- sample(1:2000,2000/2)
train <- diamonds[id,]
test <- diamonds[-id,]
#克拉和价格的关系
p <- ggplot(train, aes(x=carat,y=price))
p + geom_point()
#价格和克拉的简单线性回归
mod1 <- lm(price ~ carat,data = train)
summary(mod1)
ggplot(train,aes(x = carat,y = price)) + 
  geom_point(col = "deepskyblue",alpha = 0.1) +
  geom_abline(slope = 8303.0,intercept = -2540.0,col = "deepskyblue3",lwd = 1.5)
#多项式回归
mod2 <- lm(price ~ carat+I(carat^2)+I(carat^3),data = train)
summary(mod2)
ggplot(train,aes(x = carat,y = price)) + 
  geom_point(col = "deepskyblue",alpha = 0.1) +
  geom_smooth(method = "loess") + 
  xlim(c(0,2.5))
#多元线性回归
mod3 <- lm(price~.,data = train)
summary(mod3)
#添加变量
mod4 <- lm(price~carat+I(carat^2)+I(carat^3)+cut+color+clarity+depth+table+x+y+z,data = train)
summary(mod4)
#加入交互项
mod5 <- lm(price~carat+I(carat^2)+I(carat^3)+cut+color+clarity+depth+table+x+y+z+carat:cut+carat:color+carat:clarity,data = train)
summary(mod5)
#简化
mod6 <- lm(price~I(carat^2)+I(carat^3)+clarity+carat:cut+carat:color+carat:clarity,data = train)
summary(mod6)

#检测
test$predict.price <- predict(mod6,newdata = test)
test <- test[order(test[,8],decreasing=F),]
id <- 1:1000
test1 <- cbind(id,test)
ggplot(test1,aes(x = id,y = NULL))+ 
  geom_line(aes(y = predict.price),col = "deepskyblue") + 
  geom_line(aes(y = price),col = "deepskyblue4",lwd = 2) + 
  ylab("price")

