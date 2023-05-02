import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import glob

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

def graficar(X, numbers, plot_num, total, i):
    plt.plot(X, numbers)
    plt.text(-0.3, 8.1, f'while: {n}\nfor: {i}\ntotal: {total}')
    plt.xticks([])
    plt.savefig(f'test 1/frames/plot{plot_num}.png', dpi=300)
    plt.close ()

n = 0
plot_num = 0
total = 0
while not ordenado(numbers):
    for i in range(len(numbers) - 1):
        a = numbers[i] 
        b = numbers[i+1]
        if a > b:
            numbers[i] = b
            numbers[i+1] = a
            
            graficar(X, numbers, plot_num, total, i)
            plot_num += 1
            
        total += 1
        
    n += 1

first_image = cv2.imread('test 1/frames/plot0.png')
height, width, layers = first_image.shape

video = cv2.VideoWriter('test 1/video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 25, (width, height))

for i in range(plot_num):
    frame = cv2.imread(f'test 1/frames/plot{i}.png')
    video.write(frame)

cv2.destroyAllWindows()
video.release()

carpeta = 'test 1/frames/'
patron = carpeta + '*.png'
archivos = glob.glob(patron)

for archivo in archivos:
    os.remove(archivo)