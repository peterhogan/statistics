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
plot(circle(1E3, 6, 1), xlim = c(-15,15), ylim = c(-15,15))
