import numpy as np


numbers = [7, 4, 3, 1, 8, 9, 2, 0, 6, 5]

def ordenado(lista):
    i = lista[0]
    for j in range(1, len(lista)):
        if i > lista[j]:
            return False
        else:
            return True

while not ordenado(numbers):
    for i in range(len(numbers) - 1):
        a = numbers[i] 
        b = numbers[i+1]
        if a > b:
            numbers[i] = b
            numbers[i+1] = a
    
# for i in range(len(numbers) - 1):
#     a = numbers[i] 
#     b = numbers[i+1]
#     if a > b:
#         numbers[i] = b
#         numbers[i+1] = a

print(numbers)