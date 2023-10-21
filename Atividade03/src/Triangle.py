
from Atividade02.src.vectorized.Vec3 import Vec3
import numpy as np

class Triangle:

    def __init__(self, vertex_1: Vec3, vertex_2: Vec3, vertex_3: Vec3):
        self.__vertexes = np.array([vertex_1, vertex_2, vertex_3])
    
    @property
    def vertex_1(self):
        return self.__vertexes[0]
    
    @property
    def vertex_2(self):
        return self.__vertexes[1]
    
    @property
    def vertex_3(self):
        return self.__vertexes[2]

    def __getitem__(self, index):
        return self.__vertexes[index]