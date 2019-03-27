index = read.csv("/Users/lvanzhu/Desktop/指标.csv")
index
head(index)
names(index) = c("age","ill","diet","lav","bath","child",
                 "relat","cash","income","depos","choice")
index
number = sample(1:nrow(index),round(0.75*nrow(index)))
train = index[number,]
test = index[-number,]
maxs = apply(index,2,max)
mins = apply(index,2,min)
scaled = as.data.frame(scale(index,center = mins,scale = maxs-mins))
train_ = scaled[number,]
test_ = scaled[-number,]

library("neuralnet")
n = names(train_)
f = as.formula(paste("choice~",paste(n[!n %in% "choice"], collapse = " + ")))
f = as.formula(paste("choice~",paste(n[!n %in% "medv"], collapse = " + ")))
nn = neuralnet(f,data = train_,hidden = c(5,3),linear.output = TRUE)
nn1 = neuralnet(f,data = train_,hidden = c(5,3),linear.output = TRUE)
testprocessed = as.data.frame(test_[1:nrow(test_),])
pr.nn_ = compute(nn,testprocessed)
pr.nn_ = compute(nn,test_)
pr.nn = pr.nn_$net.result*(max(index$choice)-min(index$choice))+min(index$choice)
test.nn = test_$choice*(max(index$choice)-min(index$choice))+min(index$choice)
#mse.nn = sum((test.nn - pr.nn)^2)/nrow(test_)

par(mfrow = c(1,1))
plot(test.nn,pr.nn,xlab = "target",ylab = "output",main = paste("all : R = ",sqrt(1-sum((test.nn - pr.nn)^2)/var(test.nn))))
abline(a =0 ,b = 1,col = "red")

1-sum((test.nn - pr.nn)^2)/var(test.nn)

################
#绘图
names(index)
#,fill=盈亏
table(index$choice)
table(index$age)
p1=ggplot(index,aes(age,fill=factor(choice)))+
  geom_bar(position="stack")+
  labs(title="各省份盈亏人数分布",y="人数")
p1
  theme(plot.title = element_text(size=20,face = "bold"),
        axis.text.y=element_text(size=15),
        axis.text.x=element_text(size=10),
        axis.title.y=element_text(size=15,face="bold"),
        axis.title.x=element_text(size=15,face="bold"))
p1

transplite2 = read.csv("/Users/lvanzhu/Desktop/trainsplit3.csv")

############
#抽样
wj = read.csv("/Users/lvanzhu/Desktop/wj.csv")
transplite = read.csv("")
library(caret)
shquest[,ncol(shquest)+1] = rep(1,nrow(shquest)) 

bjquest[,ncol(bjquest)+1] = rep(0,nrow(bjquest))

questshbj = rbind(shquest,bjquest)
questshbj = questshbj[-nrow(questshbj),]
which(is.na(questshbj))
mytable=table(questshbj$V33)
prop.table(mytable) 
# 1只有0.0775 显然这个数据集是失衡的

set.seed(123)
splitindex = createDataPartition(questshbj$V33,times = 1,p = 0.5,list = FALSE)
trainsplit2 = questshbj[splitindex,]
testsplit2 = questshbj[-splitindex,]
table(trainsplit2$V33)
prop.table(table(testsplit2$V33))
set.seed(12)
ctrl = trainControl(method = "cv",number = 5)

#建立treebag模型
tbmodel = train(as.factor(V33)~.,data = trainsplit2,method = "treebag",trControl = ctrl)
predictors = names(trainsplit2)[names(trainsplit2)!='V33']
pred = predict(tbmodel$finalModel,testsplit2[,predictors])
#评估模型，用roc函数算auc得分和画图
pred = as.numeric(pred)
library(pROC)
auc = roc(testsplit2$V33,pred)
print(auc)
#auc得分0.4917不太理想(没有在0.5—1)之间
plot(auc,ylim=c(0,1),print.thres=TRUE,main=paste('AUC',round(auc$auc[[1]],2)))
abline(h=1,col="blue",lwd=2)
abline(h=0,col="red",lwd=2)
library(DMwR)
trainsplit2$V33 = as.factor(trainsplit2$V33)
trainsplit3 = SMOTE(V33~.,trainsplit2,perc.over = 900,perc.under = 100)
trainsplit2$V33 = as.numeric(trainsplit2$V33)
prop.table(table(trainsplit2$V33))

#####
#create new one
#####

#####
#create the second one
#####
