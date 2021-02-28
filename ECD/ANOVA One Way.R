clientesnuevos <- c(178, 120, 300, 400 ,500, 340,160, 111 ,200 ,201 ,140 ,70,370, 320, 150, 250, 390 ,410,210, 120 ,140, 170 ,130 ,170,450, 590 ,480 ,460 ,380 ,470)
campanya <- as.factor(c(rep(c("rojo","azul", "verde", "blanco", "amarillo"), each =6)))
boxplot(clientesnuevos ~ campanya, col = c("red","yellow", "blue", "white","green"), ylab = "Número de clientes nuevos")

test <- aov(lm(clientesnuevos~campanya))
test

summary(test)

# valor de F contraste
qf(0.05, 5-1, 30-5, lower.tail = FALSE)
