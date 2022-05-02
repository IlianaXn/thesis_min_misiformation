import numpy as np

with open('expertise/values.txt', 'w+') as f:
    for _ in range(1000000):
        f.write(f'{np.random.uniform()}\n')
