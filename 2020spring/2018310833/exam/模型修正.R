library(ggplot2)
set.seed(1234)
d <- read.csv("C:/Users/Jellysillyfish/Desktop/diamonds筛选.csv")
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

