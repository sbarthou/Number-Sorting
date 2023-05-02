import numpy as np
import time


"""
Este código revisa para cada elemento (a) en una lista si el siguiente elemento (b) es menor (if a > b) mediante un ciclo for, 
si lo es mueve el elemento (a) una posición adelante y al elemento (b) una hacia atrás. El ciclo for se ejecuta las veces necesarias mediante un ciclo while.
"""


size = int(input("Cantidad de números: "))   # solicitar cantidad de números
numbers = np.arange(size)   # generar la cantidad de números deaseados desde el 0 hasta size - 1
np.random.shuffle(numbers)   # desordenar números generados
zeros = np.zeros(size)   # array de ceros de tamaño size para generar gráfico

def ordenado(lista):   # función para deteriminar si los números están ordenados (True or False)
    i = 1
    while i < len(lista):
        if lista[i] < lista[i - 1]:
          return False
        i += 1
    return True

n = 0   # variable para contar el número de ciclos realizados
star = time.time()   # tiempo 0 
while not ordenado(numbers):
    for i in range(len(numbers) - 1):
        a = numbers[i] 
        b = numbers[i+1]
        if a > b:
            numbers[i] = b
            numbers[i+1] = a
    n += 1

end = time.time()   # tiempo final luego de ordenar los números
total = end - start   # tiempo total
print(numbers, n, total)