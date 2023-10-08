
import numpy as np


class Vec3:

    def __init__(self, x: np.float64, y: np.float64, z: np.float64):
        self.vec = np.array([x, y, z], dtype=np.float64)
    
    def __add__(self, other):
        return Vec3(self.vec[0] + other.vec[0], self.vec[1] + other.vec[1], self.vec[2] + other.vec[2])