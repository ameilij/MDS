# LOF
# Local Outlier Factor
# Factor Atípico Local para Detectar Anomalías
# Marzo 2021

# lof > 1 outlier

# Cargar librerias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

# Generar datos sintéticos para el ejemplo
# NOTE: numpy.r_ = <numpy.lib.index_tricks.RClass object>
# Translates slice objects to concatenation along the first axis.
# This is a simple way to build up arrays quickly.
X_inliers = 0.3 * np.random.randn(100,2)
X_inliers = np.r_[X_inliers + 2, X_inliers - 2]
X_outliers = np.random.uniform(low=-4, high=4, size=(20,2))
X = np.r_[X_inliers, X_outliers]

# modelo LOF para detección de outliers
clf = LocalOutlierFactor(n_neighbors=20, contamination='auto')

# las predicciones del modelo son 1 si es valor típico, -1 si es outlier
y_pred = clf.fit_predict(X)
n_outliers = sum(y_pred == -1)
n_total = len(y_pred)
X_scores = clf.negative_outlier_factor_
radius = ((X_scores.max() - X_scores) / (X_scores.max() - X_scores.min()))
print(u'El número de outliers detectados es {} de un total de {}'.format(n_outliers, n_total))

# Visualizar clasificador
fig = plt.figure(figsize=(10,5))
plt.title('Local Outlier Factor(LOF)')
plt.scatter(X[:,0], X[:,1], color='k', s=5, label='Datos')
plt.scatter(X[y_pred == 1, 0], X[y_pred == 1, 1], s=1000 * radius[y_pred == 1], edgecolors='green', facecolors='none', label='Outlier Score de Puntos Normales')

plt.scatter(X[y_pred == -1, 0], X[y_pred == -1, 1], s=1000 * radius[y_pred == -1], edgecolors='red', facecolors='none', label='Outlier Score de Puntos Atípicos')
plt.axis('tight')
plt.xlim((-5,5))
plt.ylim((-5,5))

legend = plt.legend(loc='upper left')
legend.legendHandles[0]._sizes = [10]
legend.legendHandles[1]._sizes = [20]
legend.legendHandles[2]._sizes = [20]

plt.show()