##   对p进行估计   ##
y <- matrix(c(1,0,1,1,0,0,0,0,1),9,1)
p0 <- 0.2
options(digits=4) 

loglikelihood <- function(p){
  out = sum(y*log(p)+(1-y)*log(1-p))
  return(out)
}

dl <- function(p){
  out = sum(y/p-(1-y)/(1-p))
  return(out)
}

ddl <- function(p){
  out = sum(-y/p^2-(1-y)/(1-p)^2)
  return(out)
}

hat <- function(x0,f,d,dd){
  xnew = x0
  n=50
  epsilon<-1E-4
  for(i in 1:n)
  {
    xold = xnew
    xnew = xold - d(xold)/dd(xold)
    change = abs(f(xnew)-f(xold))
    if(change < epsilon){break}
  }
  out <- xnew
  return (out)
}

Phat <- hat(p0,loglikelihood,dl,ddl)
Phat

##   对beta进行估计   ##
##探究银行客户贷款是否违约（拖欠）的问题
#数据依次为“是否违约”，“信用卡负债率”，“负债率”，“地址”，“工龄”
contract <- c(1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1,1,0)
credit <- c(11.36,1.36,.86,2.66,1.79,.39,3.83,.13,1.36,2.78,.18,.25,3.93,1.72,3.70,.82,2.92,1.18)
debt <- c(9.30,17.30,5.50,2.90,17.30,10.20,30.60,3.60,24.40,19.70,1.70,5.20,10.00,16.30,9.10,8.60,16.40,7.60)
address <- c(12,6,14,14,0,5,9,11,4,13,1,0,14,9,15,6,6,19)
seniority <- c(17,10,15,15,2,5,20,12,3,0,0,4,24,6,22,9,13,23)

y <- matrix(contract,18,1)
x <- matrix(c(rep(1,18),credit,debt,address,seniority),18,5)
b0 <- matrix(rep(0,5),5,1)

p <- function(x,b){
  out = 1/(1+exp(-x%*%b))
  return(out)
}

loglikelihood <- function(y,p){
  out = sum(y*log(p)+(1-y)*log(1-p))
  return(out)
}

dl <- function(x,y,b,p){
  out = t(x)%*%((y/p-(1-y)/(1-p))*exp(-x%*%b)/(1+exp(-x%*%b))^2)
  return(out)
}

ddl <- function(x,y,b,p){
  out = t(x)%*%(c(((-y/p^2-(1-y)/(1-p)^2)*(exp(-x%*%b)/(1+exp(-x%*%b))^2)^2
                   +(y/p-(1-y)/(1-p))*exp(-x%*%b)*(exp(-x%*%b)-1)/(1+exp(-x%*%b))^3))*x)
  return(out)
}

hat <- function(x0,x,y,p,f,d,dd){
  xnew = x0
  n = 50
  z = rep(NA,n)
  epsilon<-1E-4
  for(i in 1:n)
  {
    xold = xnew
    xnew = xold - solve(dd(x,y,xold,p(x,xold)),d(x,y,xold,p(x,xold)))
    z[i] = f(y,p(x,xnew)) 
    if(abs(f(y,p(x,xnew))-f(y,p(x,xold)))<epsilon)
    {
      plot(z[1:i],type = 'l',lwd=2,xlab = '迭代次数',ylab = '似然函数',main = '似然函数收敛曲线')                           
      break
    }
  }
  out <- xnew
  return (out)
}

BetaHat <- hat(b0,x,y,p,loglikelihood,dl,ddl)
BetaHat

cre <- glm(contract~credit+debt+address+seniority,family=binomial(link='logit'))
cre
summary(cre)

#规范化x
#判断求导正确性
#numdriv包中grad(f(x),x0)在x0处求导
#system.time记录R运行时间
#初值很重要，牛顿迭代求出的是局部最大值

data(Affairs,package = 'AER')
