circle <- function(samples,diameter,stdev) {
  datalist = list()
  
  for (i in (1:samples)) {
    p <- rnorm(1, mean = 0, sd = 1000)
    #Y <- X^2 + X - 1 + rnorm(1,mean = 0, sd = 100)
    X <- diameter*cos(3*p) + rnorm(1, sd = stdev)
    Y <- diameter*sin(3*p) + rnorm(1, sd = stdev)
    data <- data.frame(x = X, y = Y)
    datalist[[i]] <- data
  }
  
  plt.data = do.call(rbind,datalist)
  return(plt.data)
}

circ1 = circle(400, 5, 1)

#plot(circ1, xlim = c(-15,15), ylim = c(-15,15), col = 1)
dims = c(-40,40)
plot(circ1, xlim = dims, ylim = dims,col = 3)

circ1.means <- apply(circ1, 2, mean)
circ1.vars <- apply(circ1, 2,var)

estim.circ <- data.frame(x = rnorm(400, mean = circ1.means['x'], sd = circ1.vars['x']), y = rnorm(400, mean = circ1.means['y'], sd = circ1.vars['y']))
points(estim.circ, col = 2)