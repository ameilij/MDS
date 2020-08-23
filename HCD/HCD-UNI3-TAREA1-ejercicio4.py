"""
A partir de las siguientes notas de un examen:
edad = np.random.randint(15, 18, 10)
puntuacion = [3.25, 8.5, 7.75, np.nan, 9.80, 4, 6.5, np.nan, 8.70, 5.5]

1. Crea un dataframe en donde el array “edad” tenga como nombre de columna “Edad” y, para la lista “puntuación”,
  nombre “Puntuacion”.
2. Sustituye los valores nulos por 0.
3. Crea una nueva columna llamada “Situacion” que tenga como valores “PROMOCIONA” o “REPITE” en función de si
los valores de la columna “Puntuacion” son mayores a cinco o no.
4. Agrupa el nuevo dataframe por la media de edad.
5. Obtén el porcentaje de aprobados y repetidores.
6. Realiza una matriz de análisis gráfico.
7. Obtén una matriz de correlación sobre los datos numéricos.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


edad = np.random.randint(15, 18, 10)
puntuacion = [3.25, 8.5, 7.75, np.nan, 9.80, 4, 6.5, np.nan, 8.70, 5.5]

# dataframe donde array “edad” nombre “Edad” y “puntuación” nombre “Puntuacion”
dict_temp = {'edad' : edad, 'puntuacion' : puntuacion}
df = pd.DataFrame(dict_temp)
df.columns = ['Edad', 'Puntuacion']

# Sustituye los valores nulos por 0.
df['Puntuacion'] = df['Puntuacion'].fillna(0)

# Columna nueva “Situacion” como valores “PROMOCIONA” o “REPITE” en función de si
# los valores de la columna “Puntuacion” son mayores a cinco o no.
df['Situacion'] = ['PROMOCIONA' if valores > 5 else 'REPITE' for valores in df['Puntuacion']]

# Agrupa el nuevo dataframe por la media de edad.
print(df.groupby('Edad').mean())

# Obtén el porcentaje de aprobados y repetidores.
reporte = pd.crosstab(index = df['Situacion'], columns='count')/len(df)*100
reporte.columns = ['Grupo %']
print(reporte, "\n")

# Realiza una matriz de análisis gráfico
import matplotlib
from pandas.plotting import scatter_matrix
graf1 = scatter_matrix(df, figsize = (len(df.columns), len(df.columns)), diagonal='kde')
plt.show()

# Obtén una matriz de correlación sobre los datos numéricos
print(df.corr())
print("END.")
