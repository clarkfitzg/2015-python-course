ru <- read.csv('data.csv')
x <- ru[, 1]
y <- ru[, 2]

pdf('figure.pdf', height=5, width=5)

plot(x, y, col='blue')

dev.off()
