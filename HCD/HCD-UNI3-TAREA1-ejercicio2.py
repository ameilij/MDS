"""
Jugando con ARRAYS
1. Crea un array con la secuencia de números del 20 a 40 (ambos inclusive).
2. Crea un array con la secuencia de números del 20 a 40 (ambos inclusive), tomados de cinco en cinco elementos.
3. Muestra el array anterior en orden inverso.
4. Si es posible, intenta reconvertir el array reverso en un nuevo array multidimensional de 2x3.
   Si no es posible, agrega elementos al array hasta que la longitud del array sea divisible entre tres.
5. Finalmente, elimina todas las dimensiones del array y devuelve un array plano.
"""

import numpy as np

# Crear array del 20 al 40 (para incluir 40 poner 41)
arr = np.arange(20,41)

# Crear array del 20 al 40 (para incluir 40 poner 41)
# Tomar de a cinco elementos
arr_2 = np.arange(20,41,5)

# Mostrar el valor del array anterior en orden inverso
print(arr_2[::-1])

# Si es posible, intenta reconvertir el array reverso en un nuevo array multidimensional de 2x3.
# Si no es posible, agrega elementos al array hasta que la longitud del array sea divisible entre tres.
arr_2_copy = np.copy(arr_2[::-1])
arr_2_copy = arr_2_copy.reshape(2,3)
arr_2_copy

# Finalmente, elimina todas las dimensiones del array y devuelve un array plano.
arr_2_copy_2 = arr_2_copy.flaten()
