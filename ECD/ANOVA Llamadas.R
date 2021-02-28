calls <- c(420,390,480,430,440,324,450,460,450,390,430,521,320,360,342,423,355,462,286,238,344,423,123,196,321,254,412,368,340,258,433,489,238,255,366,389,198,256,248,324)
dias <- c("lunes","lunes","lunes","lunes","lunes","lunes","lunes","lunes",
          "martes","martes","martes","martes","martes","martes","martes","martes",
          "miercoles","miercoles","miercoles","miercoles","miercoles","miercoles","miercoles","miercoles",
          "jueves","jueves","jueves","jueves","jueves","jueves","jueves","jueves",
          "viernes","viernes","viernes","viernes","viernes","viernes","viernes","viernes")

llamadas <- data.frame(dias, calls)
llamadas$dias <- as.factor(llamadas$dias)
mod <- aov(calls~dias, data = llamadas)

