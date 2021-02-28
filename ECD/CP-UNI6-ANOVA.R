# ANOVA
# Caso Práctico
# Febrero 28, 2021

# Una empresa quiere determinar si las diferentes formaciones que reciben sus empleados tienen 
# influencia en el tiempo que tardan en realizar una tarea. Los doce empleados nuevos son 
# distribuidos en cuatro grupos de tres personas cada uno. A cada grupo, se le asigna 
# aleatoriamente un tipo de formación. Los resultados en la mencionada tarea, con el correspondiente 
# tipo de formación, son los siguientes:

tiempo=c(2,3,5,6,4,2,3,5,2,3,1,4)
formacion = as.factor(rep(c("1","2","3","4"),each=3))
(datos=data.frame(tiempo,formacion))

# Importar librerias
library(ggplot2)
library(ggpubr)
library(tidyverse)
library(broom)
library(AICcmodavg)

modelo <- aov(tiempo~formacion, data=datos)
summary(modelo)

TukeyHSD(modelo)
