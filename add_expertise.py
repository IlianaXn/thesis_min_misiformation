import numpy as np

with open('expertise/values.txt', 'w+') as f:
    for _ in range(1000000):
        f.write(f'{round(np.random.uniform(), 2)}\n')
