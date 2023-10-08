
import numpy as np


class Vec3:

    def __init__(self, vec: np.ndarray):
        self.vec = vec
    
    def __add__(self, other):
        return Vec3(self.vec + other.vec)