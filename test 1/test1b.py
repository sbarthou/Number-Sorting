import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

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

fig = plt.figure()
ax = plt.axes()
plt.xticks([])

frames = []

n = 0
while not ordenado(numbers):
    for i in range(len(numbers) - 1):
        a = numbers[i] 
        b = numbers[i+1]
        if a > b:
            numbers[i] = b
            numbers[i+1] = a
        
        frames.append(ax.plot(X, numbers, color='b'))
        
    n += 1
        
ani = animation.ArtistAnimation(fig, frames, interval=30, blit=True)
ani.save('video.mp4')