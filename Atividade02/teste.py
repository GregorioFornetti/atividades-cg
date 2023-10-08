import vectorized.Vec3 as Vectorized
import interactive.Vec3 as Interactive

from tqdm import tqdm
import numpy as np

current = Interactive.Vec3(0, 0, 0)
for i in tqdm(range(10000000)):
    current += Interactive.Vec3(0.1, 0.1, 0.1)

print(current)

current = Vectorized.Vec3(np.array([0, 0, 0], dtype=np.float64))
for i in tqdm(range(10000000)):
    current += Vectorized.Vec3(np.array([0.1, 0.1, 0.1], dtype=np.float64))

print(current)