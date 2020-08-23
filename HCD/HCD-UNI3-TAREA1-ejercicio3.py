"""
Ejercicio 3
1. Crea un objeto Pandas series a través de un array de 30 elementos aleatorios que sigan una distribución
beta con parámetros 0,1 y 0,8.
2. Sobre este objeto series crea un dataframe.
3. Muestra sus primeros y últimos cuatro elementos.
4. enombra la columna del dataframe a “BETA_DIST”.
5. Crea una nueva columna con nombre “SQUARE_BETA”, que sea cada elemento de la distribución beta al cuadrado.
6. Obtén los histogramas del dataframe.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import scipy

# Crea un objeto Pandas series a través de un array de 30 elementos aleatorios que sigan una distribución
# beta con parámetros 0,1 y 0,8.
mi_serie = pd.Series(np.random.beta(0.1, 0.8, 30))

# Sobre este objeto series crea un dataframe.
mi_dataframe = pd.DataFrame(mi_serie)

# Muestra sus primeros y últimos cuatro elementos.
mi_dataframe.head(4)
mi_dataframe.tail(4)

# Renombra la columna del dataframe a “BETA_DIST”.
mi_dataframe.columns = ['BETA_DIST']

# Crea una nueva columna con nombre “SQUARE_BETA”, que sea cada elemento de la distribución beta al cuadrado.
mi_dataframe['BETA_DIST_CUADRADO'] = pow(pd.Series(mi_dataframe['BETA_DIST']),2)

# Obten los histogramas del dataframe
mi_dataframe.hist(figsize=(len(mi_dataframe.columns), len(mi_dataframe.columns)))

# Obtén los histogramas del dataframe (AUTOMÁTICO)
mi_dataframe.hist()

# BONUS: plot de la probability density function
grafico = mi_dataframe.plot.kde()
plot.show()
