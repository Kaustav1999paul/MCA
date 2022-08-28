x <- c(151, 174, 138, 544,522,122,452,532)
y <- c(67,44,89,45,67,89,34,22)

relation <- lm(y-x)
print(relation)


plot(y, x, col="blue", main="Hello", abline(ln(x~y)), cex=1.3, pch=16, xlab="Weight", ylab="Height")

