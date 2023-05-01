import numpy as np
import matplotlib.pyplot as plt


num = [7, 4, 3, 1, 8, 9, 2, 0, 6, 5]
snum = np.zeros(len(num))


def menor_mayor(a, b):
    if a < b: return True
    else: return False


m = 0
for i in range(len(num)):
    
    for j in range(1, len(num)):
        n = j
        if num[i] < num[j] and num[j] not in snum:
            snum[m] = num[j]
            m += 1
            break
        
    for k in range(n+1, len(num)):
        if num[i] < num[k]:
            snum[m] = num[k]
            m += 1
            break
        
        
print(snum) 