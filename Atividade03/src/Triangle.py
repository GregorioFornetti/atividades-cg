
from Atividade02.src.vectorized.Vec3 import Vec3
import numpy as np

class Triangle:

    def __init__(self, vertex_1: Vec3, vertex_2: Vec3, vertex_3: Vec3):
        '''
        Construtor da classe Triangle. Atualmente, apenas recebe os 3 vértices do triângulo.

        ---

        Parâmetros:

            - vertex_1: Vec3 - Primeiro vértice do triângulo.

            - vertex_2: Vec3 - Segundo vértice do triângulo.

            - vertex_3: Vec3 - Terceiro vértice do triângulo.
        '''
        self.__vertexes = np.array([vertex_1, vertex_2, vertex_3])
    
    @property
    def vertexes(self) -> np.ndarray:
        '''
        Retorna um array contendo os vértices do triângulo.
        '''
        return self.__vertexes
    
    @property
    def vertex_1(self) -> Vec3:
        '''
        Primeiro vértice do triângulo.
        '''
        return self.__vertexes[0]
    
    @property
    def vertex_2(self) -> Vec3:
        '''
        Segundo vértice do triângulo.
        '''
        return self.__vertexes[1]
    
    @property
    def vertex_3(self) -> Vec3:
        '''
        Terceiro vértice do triângulo.
        '''
        return self.__vertexes[2]

    def __getitem__(self, index) -> Vec3:
        '''
        Retorna o vértice especificado.

        0 = primeiro vértice, 1 = segundo vértice, 2 = terceiro vértice.
        '''
        return self.__vertexes[index]