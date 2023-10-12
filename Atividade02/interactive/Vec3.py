
from typing import Union
import numpy as np


class Vec3:

    def __init__(self, x: np.float64 = 0.0, y: np.float64 = 0.0, z: np.float64 = 0.0):
        self.vec = np.array([x, y, z], dtype=np.float64)
    

    def x(self) -> np.float64:
        return self.vec[0]
    
    def y(self) -> np.float64:
        return self.vec[1]
    
    def z(self) -> np.float64:
        return self.vec[2]
    

    def __neg__(self) -> 'Vec3':
        return Vec3(-self.vec[0], -self.vec[1], -self.vec[2])
    
    def __getitem__(self, key: int) -> np.float64:
        return self.vec[key]
    

    def __add__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] + other.vec[0], self.vec[1] + other.vec[1], self.vec[2] + other.vec[2])
        else:
            return Vec3(self.vec[0] + other, self.vec[1] + other, self.vec[2] + other)
    
    def __sub__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] - other.vec[0], self.vec[1] - other.vec[1], self.vec[2] - other.vec[2])
        else:
            return Vec3(self.vec[0] - other, self.vec[1] - other, self.vec[2] - other)
    
    def __mul__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] * other.vec[0], self.vec[1] * other.vec[1], self.vec[2] * other.vec[2])
        else:
            return Vec3(self.vec[0] * other, self.vec[1] * other, self.vec[2] * other)
    
    def __truediv__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] / other.vec[0], self.vec[1] / other.vec[1], self.vec[2] / other.vec[2])
        else:
            return Vec3(self.vec[0] / other, self.vec[1] / other, self.vec[2] / other)


    def __iadd__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            self.vec[0] += other.vec[0]
            self.vec[1] += other.vec[1]
            self.vec[2] += other.vec[2]
        else:
            self.vec[0] += other
            self.vec[1] += other
            self.vec[2] += other
        return self
    
    def __isub__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            self.vec[0] -= other.vec[0]
            self.vec[1] -= other.vec[1]
            self.vec[2] -= other.vec[2]
        else:
            self.vec[0] -= other
            self.vec[1] -= other
            self.vec[2] -= other
        return self
    
    def __imul__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            self.vec[0] *= other.vec[0]
            self.vec[1] *= other.vec[1]
            self.vec[2] *= other.vec[2]
        else:
            self.vec[0] *= other
            self.vec[1] *= other
            self.vec[2] *= other
        return self

    def __itruediv__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        if isinstance(other, Vec3):
            self.vec[0] /= other.vec[0]
            self.vec[1] /= other.vec[1]
            self.vec[2] /= other.vec[2]
        else:
            self.vec[0] /= other
            self.vec[1] /= other
            self.vec[2] /= other
        return self
    
    def __repr__(self) -> str:
        return f"{self.vec[0]} {self.vec[1]} {self.vec[2]}"
    
    
    def length(self) -> np.float64:
        return np.sqrt(self.squared_length())
    
    def squared_length(self) -> np.float64:
        return self.vec[0] ** 2 + self.vec[1] ** 2 + self.vec[2] ** 2
    
    def dot(self, other: 'Vec3') -> np.float64:
        return self.vec[0] * other.vec[0] + self.vec[1] * other.vec[1] + self.vec[2] * other.vec[2]
    
    def cross(self, other: 'Vec3') -> 'Vec3':
        return Vec3(self.vec[1] * other.vec[2] - self.vec[2] * other.vec[1],
                    self.vec[2] * other.vec[0] - self.vec[0] * other.vec[2],
                    self.vec[0] * other.vec[1] - self.vec[1] * other.vec[0])
    
    def unit_vector(self) -> 'Vec3':
        return self / self.length()
