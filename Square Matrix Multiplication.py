"""El programa es simple, toma un array como argumento y lo multiplica con la funcion np.dot(), el resultado es el produxto de una matriz"""
import numpy as np

def multiplicar_matrices(a, b):
    return np.dot(a,b).tolist()

print(multiplicar_matrices([ [1, 2], [3, 2] ], 
    [ [3, 2],
    [1, 1] ]))