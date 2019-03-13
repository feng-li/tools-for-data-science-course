
mchol=function(x)
{
  mn=dim(x)                                                         #x的维数
  m=mn[1]                                                           #x的行数
  n=mn[2]                                                           #x的列数
  if(m!=n) return ("Wrong dimensions of matrix!")                   #检验x是否是方阵
  if(sum(t(x)!=x)>0) return ("Input matrix is not symmetrical!")    #检验x是否是对称阵
  L=matrix(0,m,m)                                                   #先给L定义一个空矩阵
  for(i in 1:m)
    {
      L[i,i]=sqrt(x[i,i])                                           #L矩阵(1,1)位置的元素等于x11的平方根
      if(i<m)
      {
        L[(i+1):m,i]=x[(i+1):m,i]/L[i,i]                            #计算向量(L21,...,Lm1),m-i维的
        TLV=L[(i+1):m,i]                                            #给(L21,...,Lm1)一个定义
        TLM=matrix(TLV,m-i,m-i)                                     #将TLV按照列排成一个m-i维的矩阵
        TLM=sweep(TLM,2,TLV,"*")                                    #新的TLM矩阵是每列都乘以TLV
        x[(i+1):m,(i+1):m]=x[(i+1):m,(i+1):m]-TLM                   #减去TLM之后得到一个新的可做cholesky分解的矩阵
      }
    }
  L                                                                 #返回L  
}

######EXAM
#y=matrix(rnorm(20),5)#
#x=t(y)%*%y
#mchol(x)
#t(chol(x))                                                         #因为R中的分解函数解出来是一个上三角矩阵，转置一下
######EXAM


mforwardsolve=function(L,b)                                                 
{
  mn=dim(L); m=mn[1]; n=mn[2]                                               
  if(m!=n) return ("Wrong dimensions of matrix L!")                         
  if(m!=length(b)) return ("Wrong dimensions of matrix L or vector b!")   
  x=rep(0,m)                                                             
  for(i in 1:m)
  {
    x[i]=b[i]/L[i,i]
    if(i<m) b[(i+1):m]=b[(i+1):m]-x[i]*L[(i+1):m,i]      
  }
  x  
}
mbacksolve=function(L,b){
  mn=dim(L); m=mn[1]; n=mn[2]
  if(m!=n) return ("Wrong dimensions of matrix L!")
  if(m!=length(b)) return ("Wrong dimensions of matrix L or vector b!")
  x=rep(0,m)
  for(i in m:1){
    x[i]=b[i]/L[i,i]
    if(i>1) b[(i-1):1]=b[(i-1):1]-x[i]*L[(i-1):1,i]      
  }
  x  
}
######EXAM
#y=matrix(rnorm(20),5)
#x=t(y)%*%y
#L=mchol(x); b=1:4
#mforwardsolve(L,b)
#forwardsolve(L,b)
######EXAM

ridgereg=function(lambda,x,y)
{
  #y=data[,m]; x=data[,-m]这句话意思是取数据的第几列作为因变量
  np=dim(x)
  n=np[1]
  p=np[2]
  x=as.matrix(cbind(rep(1,n),x))                                   #加入截距项
  V=t(x)%*%x+diag(c(0,rep(lambda,p)))                              #要cholesky分解的矩阵
  U=as.vector(t(x)%*%y)
  R=mchol(V)
  M=mforwardsolve(R,U)
  mbacksolve(t(R),M)   
}

pred=function(b,nx)
{
  #nx=prostate[1:2,1:8]
  b=as.vector(b)
  p=length(b)-1
  nx=as.matrix(nx,ncol=p)
  n=dim(nx)[1]
  apply(t(nx)*b[2:(p+1)],2,sum)+b[1]  
}

cvridgeregerr=function(lambda,x,y){  
  mridge=function(i,lambda,x,y) ridgereg(lambda,x[-i,],y[-i])
  #lambda=1
  np=dim(x);n=np[1];p=np[2]
  coe=t(apply(as.matrix(1:n,ncol=1),1,mridge,lambda,x,y))
  mean((apply(coe*cbind(1,x),1,sum)-y)^2)
}

ridgeregerr=function(lambda,x,y)mean((pred(ridgereg (lambda,x,y),x)-y)^2)
###############################
library(ElemStatLearn)
x=prostate[,1:8]; y=prostate[,9]
LAM=seq(0.001,10,len=50)
err=unlist(lapply(LAM,ridgeregerr,x,y))
pe=unlist(lapply(LAM,cvridgeregerr,x,y))
x=rep(1:50,2)
type=rep(1:2,c(50,50))
interaction.plot(x,type,c(err,pe))

###############################################

library(ElemStatLearn)
x=prostate[,1:8]; y=prostate[,9]
ridgereg(data[,1:9],lambda=1)
library(mda)
ridge1=gen.ridge(prostate[,1:8], y=prostate[,9,drop=FALSE], lambda=1)  
ridge1$coe

