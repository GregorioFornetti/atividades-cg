import numpy as np
import time

vec = np.array([0, 0, 0], dtype=np.float64)

start = time.time()
for _ in range(100000000):
    vec += np.array([0.1, 0.1, 0.1], dtype=np.float64)

print(vec)
print(time.time() - start)