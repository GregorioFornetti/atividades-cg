
from Atividade02.src.vectorized.Vec3 import Point3
from Atividade04.src.classes.Hittable import Hittable
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.HitRecord import HitRecord
from Atividade04.src.classes.Interval import Interval
import numpy as np


class Triangle(Hittable):

    def __init__(self, vertex_1: Point3, vertex_2: Point3, vertex_3: Point3):
        self.__vertexes = np.array([vertex_1, vertex_2, vertex_3])
    
    @property
    def vertexes(self) -> np.ndarray:
        '''
        Retorna um array contendo os vértices do triângulo.
        '''
        return self.__vertexes
    
    @property
    def vertex_1(self) -> Point3:
        return self.__vertexes[0]
    
    @property
    def vertex_2(self) -> Point3:
        return self.__vertexes[1]
    
    @property
    def vertex_3(self) -> Point3:
        return self.__vertexes[2]
    
    def __getitem__(self, index) -> Point3:
        '''
        Retorna o vértice especificado.

        0 = primeiro vértice, 1 = segundo vértice, 2 = terceiro vértice.
        '''
        return self.__vertexes[index]

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        # Descobrindo o vetor normal
        v1_to_v2 = self.vertex_2 - self.vertex_1
        v1_to_v3 = self.vertex_3 - self.vertex_1
        normal = v1_to_v2.cross(v1_to_v3)

        # Descobrindo o valor P: intersecção do raio com o plano formado pelo triângulo
        normal_dot_ray_dir = normal.dot(ray.direction)
        if normal_dot_ray_dir == 0:
            return False, None  # O raio é paralelo ao plano
        
        d = -normal.dot(self.vertex_1)
        t = -(normal.dot(ray.origin) + d) / normal_dot_ray_dir

        if t not in t_interval:
            return False, None  # O triângulo está atrás do raio
        
        intersect_point = ray.at(t)

        # Verificando se o ponto de intersecção está dentro ou fora do triângulo
        # Todo lugar que retornar False, quer dizer que o ponto está à direita da aresta, logo, fora do triângulo
        # Só estará dentro do triângulo se para todas as arestas, o ponto estiver para esquerda
        edge_1 = self.vertex_2 - self.vertex_1
        vp1= intersect_point - self.vertex_1
        c = edge_1.cross(vp1)
        if normal.dot(c) < 0:
            return False, None
        
        edge_2 = self.vertex_3 - self.vertex_2
        vp2= intersect_point - self.vertex_2
        c = edge_2.cross(vp2)
        if normal.dot(c) < 0:
            return False, None

        edge_3 = self.vertex_1 - self.vertex_3
        vp3= intersect_point - self.vertex_3
        c = edge_3.cross(vp3)
        if normal.dot(c) < 0:
            return False, None
        
        return True, HitRecord(intersect_point, normal, t, ray)