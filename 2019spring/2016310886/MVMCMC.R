# muilti-variable Metropolis algorithm
# author = 恕 from CUFE
# last edited in 2018.6.15
# "MCMC.RData" required
# package "mvtnorm" required
# package "rgl" required
# package "scatterplot3d" required
rm(list = ls())
graphics.off()
cat('\014')

MVMCMC = function(p,
                step = 50000,
                x0 = rep(0,n),
                burn = max(1,as.integer(step/100)),
                df = 3*matrix(c(1,0.3,0.3,1),2),
                n = 2,
                plot_x = TRUE,
                plot_alpha = TRUE,
                plot_hist = TRUE,
                plots = TRUE,
                windows = TRUE
                ){
library(mvtnorm)
library(rgl)
library(scatterplot3d)
    
{# customizing 
# # dimension
# n = 2
# # target distribution function
# p = function(x)
# return(dmvnorm(x,
#             mean = rep(0,2),
#             sigma = matrix(c(1,0.3,0.3,1),2),
#             log = FALSE))
# # starting value
# x0 = matrix(rep(0,n),n,1)
# # maximum of simulation and the steps to be burned
# step = 50000
# burn = max(1,as.integer(step/100))
# # standard deviation from the random walk
# df = 3*matrix(c(1,0.3,0.3,1),2)
# windows = TRUE
# plot_x = TRUE
# plot_alpha = TRUE
# plot_hist = TRUE
# plots = TRUE
}# customizing section
if(step<50)
warning("too few steps")

{# initialising
x = matrix(1,n,step)
x[1:n,1] = x0
alpha = matrix(1,1,step)
}# initialising
    
for (i in 1:(step-1)){# main loop
    # the former x
    x_old = x[1:n,i]
    # random generate a new x
    x_temp = rmvnorm(1,x_old,df)
    # calculate alpha
    alpha[i] = min(1,p(x_temp)/p(x_old))
    # renew x 
    flag = runif(1)
    x[1:n,i+1] = x_temp*(flag<alpha[i]) + x_old*(flag>alpha[i])
}# main loop
x_use = x[1:n,burn:step]

{# plotting section
if(plots == FALSE){
    plot_x = FALSE
    plot_alpha = FALSE
    plot_hist = FALSE
}
# alpha vs steps
if(plot_alpha == TRUE){
    if(windows == TRUE)
        windows()
    plot(burn:step,alpha[1,burn:step],
        type = 'p',
        pch = '.',
        main = "Each Step of alpha",
        xlab = "step (counting from burn)",
        ylab = "x"
        )
}
# x vs steps
if (plot_x==TRUE){
    if(windows==TRUE)
        open3d()
    plot3d(x_use[1,],x_use[2,],
           #type = 'l',
           main = "Each Step of x",
           xlab = "step (counting from burn)",
           zlab = "x",
           ylab = "y"
           )
}
# 3d hist
if (plot_hist == TRUE){
    open3d()
    # breaks of x and y values
    breaks = 80
    # preparation
    x = x_use[1,];y = x_use[2,]
    xmin = min(x);xmax = max(x);ymin = min(y);ymax = max(y)
    xlen = xmax-xmin;ylen = ymax-ymin
    xgap = xlen/breaks;ygap = ylen/breaks

    # a painful process to count z
    z = matrix(0,breaks,breaks)
    for (i in 1:breaks){
        for (j in 1:breaks){
        z[i,j] = sum(((x>(xmin+(i-1)*xgap))
                     +(x<(xmin+i*xgap))
                     +(y>(ymin+(j-1)*ygap))
                     +(y<(ymin+j*ygap))
                     )==4)
    }
    }

    # x and y axis values
    xa1 = seq(xmin,xmax,length.out = breaks)
    ya1 = seq(ymin,ymax,length.out = breaks)
    xa = as.vector(matrix(rep(xa1,breaks),breaks))
    ya = as.vector(t(matrix(rep(ya1,breaks),breaks)))

    # generated points
    plot3d(xa,ya,
           z/sum(z),
           col = 'red',
           xlab = "x",
           ylab = "y",
           zlab = "frequency"
           )

    # target points
    z_ideal = matrix(p(cbind(xa,ya)),breaks)
    plot3d(xa,ya,
           z_ideal/sum(z_ideal),
           col = 'blue',
           add = TRUE
           )
}
}# plotting section

return(x_use)
}


# # examples----
# p = function(x)
# return(dmvnorm(x,
#             mean = rep(0,2),
#             sigma = matrix(c(1,0.3,0.3,1),2),
#             log = FALSE))
# 
# x = MVMCMC(p)
# cat('\014')


