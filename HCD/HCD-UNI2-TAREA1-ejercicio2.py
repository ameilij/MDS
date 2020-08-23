"""
Dado el siguiente diccionario de datos:

precios = {
    'ACCIONA': [78.60, 84.95, 77.20],
    'ACERINOX': [5.88, 51.25, 58.42],
    'INDITEX': [49.99, 57.89, 68.5],
    'ENEGAS': [0.5, 0.78, 48.75],
    'FERROVIAL': [78.58, 24.25, 65.45]
}

Modificar cualquier precio inferior a 50, por el valor 50 y, finalmente, devolver el diccionario de datos actualizado por cada nombre de empresa.
"""
precios = {
    'ACCIONA': [78.60, 84.95, 77.20],
    'ACERINOX': [5.88, 51.25, 58.42],
    'INDITEX': [49.99, 57.89, 68.5],
    'ENEGAS': [0.5, 0.78, 48.75],
    'FERROVIAL': [78.58, 24.25, 65.45]

# La siguiente solución es un ejemplo de como iterar en diccionarios condicionalmente
for key in precios:
    precios[key] = [50 if precio < 50 else precio for precio in precios[key]]

print(precios)
