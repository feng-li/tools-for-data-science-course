# Metropolis-Hasting
# author = 恕 from CUFE
# last edited in 2018.7.10
# MCMC.RData required
rm(list = ls())
graphics.off()
cat('\014')

MH = function(p,
              q = function(x)
                  return(dnorm(x,1,3)),
              rq = function()
                   return(MCMC(q,
                               step = 50,
                               plots = FALSE
                               )[50]),
              step = 10000,
              x0 = 0,
              burn = max(1,as.integer(step/100)),
              plot_x = TRUE,
              plot_alpha = TRUE,
              plot_hist = TRUE,
              plots = TRUE,
              windows = TRUE
              ){
    #!!! MCMC.RData required!!!
{# help 
# The Metropolis-Hasting algorithm ,which is based on MCMC,
# can also be used to generate a series of random numbers
# obeying given distribution.
# 
# 'p' is density function of the given distribution.
# It must be a one-variable density function.
# 
# Instead of using random walk proposal, this algorithm 
# generates new candidates all obeying to another 
# distribution 'q(x)'. In order to gain best results, it
# is recommended that 'q(x)' should be similiar to 'p(x)'.
# 
# 'q' is the density func, and 'rq' is the func used to
# generte new candidates. A normol distribution and a 
# MCMC method are set as default.
# But the default rq is not recommended as the efficiency
# is too low
# 
# Then an accept rate 'alpha' is calculated according to
# 'p','q',x-old' and 'x-temp'. Unlike basic MCMC, 'q' is
# also involved.
# The x-new will equal to x-temp with probability 'alpha'
#  and x-old with prob '1-alpha'.
# 
# 'step' is the total numbers generated. Since the Markov
# chian may have not convergenced in the first values,
# they have to be "burned".
# 'burn' controls how many numbers will be abandoned.
# 
# This function provides 3 figures
# 'plot_x" draws x-vs-step figure
# 'plot_alpha' draws alpha-vs-step figure
# 'plot_hist' draws ahistgram of x and the theoretical
# density line (marked with blue)
# 'plot' = FALSE shuts down all graphic outputs
# 
# The return value is a matrix containing each step of x.
# The total length is 'step - burn'
}# help 
load("MCMC.Rdata")

{#customizing section
# # target distribution function
# p = function(x)
#     return(df(x,20,10))
# # the function to simulate target func
# q = function(x)
#     return(dnorm(x,1.5,3))
# # starting value
# x0 = 1
# # maximum of simulation and the steps to be burned
# step = 10000
# burn = max(1,as.integer(step/100))
# 
# plot_x = TRUE
# plot_alpha = TRUE
# plot_hist = TRUE
# plot = TRUE
}#customizing section

{# initialising
x = matrix(1,1,step)
x[1,1] = x0
alpha = matrix(1,1,step)
}# initialising

# main loop
for (i in 1:(step-1)){
    # the former x
    x_old = x[1,i]
    # random generate a new x
    x_temp = rq()
    # calculate alpha
    alpha[i] = min(1,p(x_temp)*q(x_old)/p(x_old)/q(x_temp))
    # renew x
    flag = runif(1)
    x[1,i+1] = x_temp*(flag<alpha[i])+x_old*(flag>alpha[i])
}
x_use = x[1,burn:step]

{# plotting section
if(plots == FALSE){
    plot_x = FALSE
    plot_alpha = FALSE
    plot_hist = FALSE
}
# x vs steps
if (plot_x==TRUE){
    if(windows==TRUE)
        windows()
    if(plot_x==TRUE&plot_alpha == TRUE){
        par(mfrow=c(2,1))
    }
    plot(burn:step,x_use,type = 'l',
        main = "Each Step of x",
        xlab = "step (counting from burn)",
        ylab = "x"
        )
}
# alpha vs steps
if(plot_alpha == TRUE){
    if(plot_x==FALSE&plot_alpha == TRUE&windows == TRUE)
        windows()
    plot(burn:step,alpha[1,burn:step],
        type = 'p',
        pch = '.',
        main = "Each Step of alpha",
        xlab = "step (counting from burn)",
        ylab = "x"
        )
}
# histgram of x and theoretical density line(blue)
if (plot_hist == TRUE){
    if(windows == TRUE|plot_x == TRUE|plot_alpha == TRUE)
        windows()
    hist(x_use,
         breaks = 100,
         freq = FALSE,
         main = "MH\n Histgram of x and Theoretical Density",
         xlab = "x",
         ylab = "density"
         )

    range = seq(min(x),max(x),(max(x)-min(x))/100)
    y1 = p(range)
    lines(range,y1,
          col = 'blue',
          lwd = 3
          )
    y2 = q(range)
    lines(range,y2,
          col = 'purple',
          lwd = 3
          )
    legend("topright",fill = c("blue","purple"),
           expression("target","simulation"))
}
}# plotting section

return(x_use)
}


# examples----
p = function(x)dnorm(x,0,3)

{# the effect of q
q1 = function(x)dnorm(x,0,4)
rq1 = function()return(rnorm(1,0,4))

df = sqrt(5/3)
q2 = function(x)dt(x,df)
rq2 = function()return(rt(1,df))

windows()
par(mfrow =c(2,1))
MH(p,q1,rq1,10000,
   plot_x = FALSE,plot_alpha = FALSE,windows = FALSE)
MH(p,q2,rq2,10000,
   plot_x = FALSE,plot_alpha = FALSE,windows = FALSE)

# we can observe no significant differences
}# the effect of q

{# the effect of rq
q = function(x)dnorm(x,0,4)
rq1 = function()return(rnorm(1,0,4))

windows()
par(mfrow =c(2,1))
MH(p,q,rq1,step = 10000,
   plot_x = FALSE,plot_alpha = FALSE,windows = FALSE)
MH(p,q,step = 10000,
   plot_x = FALSE,plot_alpha = FALSE,windows = FALSE)

# That's why default rq is not recommended
# To improve effeciency, only minimun iterations of MCMC
# are calculated. Thus the effect may not be so well
#
# only use default rq as last resort
}# the effect of rq

{# comparison with MCMC
load("MCMC.Rdata")
windows()
par(mfrow = c(2,1))
MH(p,q,rq1,100000,
   plot_x = FALSE,plot_alpha = FALSE,windows = FALSE)
MCMC(p,plot_x = FALSE,plot_alpha = FALSE,windows = FALSE)

# personally, I really dislike MH :(
}# comparison with MCMC




cat('\014')


