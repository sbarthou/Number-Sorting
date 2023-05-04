import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FFMpegWriter


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

fig = plt.figure(figsize=(10, 6))
plt.xticks([])
line, = plt.plot(X, numbers)
text = plt.text(0.3, (size - 5), [], fontsize=8)

plt.xlim(0, size)
plt.ylim(0, size)

metadata = dict(title='Movie', artist='sbarthou')
writer = FFMpegWriter(fps=360, metadata=metadata)

n = 0
plot_num = 0
total = 0
with writer.saving(fig, 'test 1/test1f.mp4', 300):
    line.set_data(X, numbers)
    text.set_text(f'while: none\nfor: none\ntotal: none\nFrame: none')
    writer.grab_frame()
    plot_num += 1
    while not ordenado(numbers):
        for i in range(len(numbers) - 1):
            a = numbers[i] 
            b = numbers[i+1]
            if a > b:
                numbers[i] = b
                numbers[i+1] = a
                
                line.set_data(X, numbers)
                text.set_text(f'while: {n}\nfor: {i}\ntotal: {total}\nFrame: {plot_num}')
                writer.grab_frame()
                plot_num += 1
                
            total += 1
                
        n += 1