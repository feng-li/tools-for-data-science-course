library(ggplot2)    
set.seed(1234)
d <- read.csv("C:/Users/Jellysillyfish/Desktop/diamonds筛选.csv")
diamonds <- d[sample(1:6689,1000),]
p <- ggplot(diamonds, aes(x=carat,y=price))
#绘制散点图
p + geom_point()
p1 <- ggplot(diamonds,aes(x = price)) + 
  #以价格为x轴绘制核密度图
  geom_density(lwd = 1) +
  #添加标题 
  ggtitle("Density of Price") 
p1
p2 <- ggplot(diamonds,aes(x = price)) + 
  #以价格为x轴，按照切工分组绘制核密度图
  geom_density(lwd = 1,aes(color = cut)) + 
  #调整图例位置
  theme(legend.position = c(0.85,0.7)) +
  #添加标题 
  ggtitle("Price,by CUT")
p2
p3 <- ggplot(diamonds,aes(x = price)) + 
  geom_density(lwd = 1,aes(color = color)) + 
  theme(legend.position = c(0.91,0.6)) + 
  ggtitle("Price,by Color")
p3
p4 <- ggplot(diamonds,aes(x = price)) + 
  geom_density(lwd = 1,aes(color = clarity)) + 
  theme(legend.position = c(0.9,0.56)) + 
  ggtitle("Price,by Clarity")

p4