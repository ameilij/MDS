# PCA
# Principal Component Analysis
# Reducción de Dimensionalidad
# Marzo 2021

# De x1, x2,...,xp, obtener x1', x2',...,xm', donde m < p

# Cargar librerias
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# Cargar juego de datos
dataset = load_iris()
X = dataset.data
Y = dataset.target

print(u'El número total de variables del dataset es: {}'.format(X.shape[1]))

# Representar variables 0 y 1
plt.scatter(X[:,0], X[:,1], c=Y)
plt.title(u'Representación de 2 variables')
plt.xlabel(dataset.feature_names[0])
plt.ylabel(dataset.feature_names[1])
plt.show()

# PCA
# ===

# Escalar variables antes de PCA
scaler = StandardScaler()
X_escaladas = scaler.fit_transform(X)

# Ajustar PCA
pca = PCA()
pca.fit(X_escaladas)

# Visualizar la varianza explicada
plt.plot(range(1,5), pca.explained_variance_ratio_, c="orange")
plt.bar(range(1,5), np.cumsum(pca.explained_variance_ratio_))
plt.xlabel(u'Número de componentes principales')
plt.ylabel(u'Proporción de varianza explicada')
plt.ylim(0,1)
plt.axhline(0.90, c='blue')
plt.show()

# Es difícil seguir en el programa, pero en el cuadro anterior se nota que cuando n=2,
# obtenemos el 90% de la varianza, por lo que dos componentes son suficientes para
# nuestro modelo PCA
pca = PCA(n_components=2)
pca.fit(X_escaladas)
comp_principales = pca.transform(X_escaladas)

# La forma de visualizarlo es la siguiente
plt.scatter(comp_principales[:,0], comp_principales[:,1], c=Y)
plt.title(u'Representación de las dos primeras componentes principales')
plt.xlabel('Componente 1')
plt.ylabel('Componente 2')
plt.show()
