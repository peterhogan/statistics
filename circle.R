polynomial <- list()

for (i in (1:500)) {
  sdRnd <- abs(rnorm(1,mean = 1000, sd = 350))
  X <- rnorm(1, mean = 0, sd = 4)
  Y <- 4*X^3 - 2*X^2 + X + rnorm(1, mean = 0, sd = sdRnd)
  data <- data.frame(x = X, y = Y)
  polynomial[[i]] <- data
}

poly = do.call(rbind, polynomial)

plot(poly)