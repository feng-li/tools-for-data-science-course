# Markov-chain Monte Carlo(Metropolis algorithm)
# author = 恕 from CUFE
# last edited in 2018.6.15
rm(list = ls())
graphics.off
cat('\014')


MCMC = function(p,
                step = 100000,
                x0 = 0,
                burn = max(1,as.integer(step/100)),
                df = 3,
                plot_x = TRUE,
                plot_alpha = TRUE,
                plot_hist = TRUE,
                plots = TRUE,
                windows = TRUE
){
{# help
# The Metropolis algorithm generates random numbers which 
# obeys a given distribution. Those numbers actually forms
# a Markov chain.
# 
# 'p' is density function of the given distribution.
# It must be a one-variable density function.
# 
# 'x0' is the first value in the chain. Actually the final
# results rely little on it.
# 
# To generate a new value from the old one, a method called
# 'random walk' is applyed and one significant value is 
# the standard deviation of the normal distribution, which
# can be modified by varable 'df'. Anyway, we get a 
# candidate 'x-temp'
# 
# Then an accept rate 'alpha' is calculated according to
# 'p','x-old' and 'x-temp'. The x-new will equal to x-temp
# with probability 'alpha' and x-old with prob '1-alpha'.
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
if(step<50)
warning("too few steps")

{# customizeing section
# target distribution function
#p = function(x)
#return(dt(x,5,log = FALSE))
# starting value
#x0 = 0
# maximum of simulation and the steps to be burned
#step = 100000
#burn = max(1,as.integer(step/100))
# standard deviation from the random walk
#df = 3
}# customizing section
    
{# initialising
x = matrix(1,1,step)
x[1,1] = x0
alpha = matrix(1,1,step)
}# initialising
    
for (i in 1:(step-1)){# main loop
    # the former x
    x_old = x[1,i]
    # random generate a new x
    x_temp = rnorm(1,x_old,df)
    # calculate alpha
    alpha[i] = min(1,p(x_temp)/p(x_old))
    # renew x 
    flag = runif(1)
    x[1,i+1] = x_temp*(flag<alpha[i]) + x_old*(flag>alpha[i])
}# main loop
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
         main = "MCMC\n Histgram of x and Theoretical Density",
         xlab = "x",
         ylab = "density"
         )

    range = seq(min(x),max(x),0.1)
    y = p(range)
    lines(range,y,
          col = 'blue',
          lwd = 3
          )
}
}# plotting section

return(x_use)
}


# examples----

#p = function(x)
#   return(dt(x,5,log = FALSE))
#x = MCMC(p,step = 1000)
#
#windows()
#par(mfrow = c(2,1))
#x1 = MCMC(p,x0 = 0,     plot_x = FALSE,plot_alpha = FALSE)
#x2 = MCMC(p,x0 = 10,   plot_x = FALSE,plot_alpha = FALSE)
# we can see from the two exampls that X0 has little 
# effect on the final results

#windows()
#par(mfrow = c(2,1))
#x3 = MCMC(p,df = 1000,    plot_hist = FALSE,plot_alpha = FALSE)
#x4 = MCMC(p,df = 0.001,   plot_hist = FALSE,plot_alpha = FALSE)
# these examples tells us the importance of a proper df

# another p(x)
#p1 = function(x)
#    return(dnorm(x,0,10))
#windows()
#par(mfrow = c(2,1))
#x5 = MCMC(p1,plot_hist = FALSE)
#windows()
#x5 = MCMC(p1,plot_x = FALSE,plot_alpha = FALSE)





cat('\014')
