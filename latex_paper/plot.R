ru <- read.csv('data.csv')

pdf('figure.pdf', height=5, width=5)
plot(ru$x, ru$y, xlab='x', ylab='f(x)', col='red')
dev.off()
