import numpy as np
import matplotlib.pyplot as plt


size = int(input("Cantidad de números: "))
numbers = np.arange(size)
np.random.shuffle(numbers)
X = np.arange(size)

def ordenado(lista):
    i = 1
    while i < len(lista):
        if lista[i] < lista[i - 1]:
          return False
        i += 1
    return True

plt.ion()
fig, ax = plt.subplots(figsize=(10, 7))
plot, = ax.plot(X, numbers)

n = 0
while not ordenado(numbers):
    if n < 1:
        fig.canvas.draw()
    for i in range(len(numbers) - 1):
        a = numbers[i] 
        b = numbers[i+1]
        if a > b:
            numbers[i] = b
            numbers[i+1] = a
       
            plot.set_xdata(X)
            plot.set_ydata(numbers)    
    
            fig.canvas.draw()
            fig.canvas.flush_events()
    
    n += 1