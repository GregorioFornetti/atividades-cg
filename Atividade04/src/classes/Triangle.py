
from typing import Union

from Atividade02.src.vectorized.Vec3 import Point3, Vec3
from Atividade04.src.classes.Hittable import Hittable
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.HitRecord import HitRecord
from Atividade04.src.classes.Interval import Interval

import numpy as np


class Triangle(Hittable):

    def __init__(self, vertex_1: Point3, vertex_2: Point3, vertex_3: Point3, normals: 'list[Point3, Point3, Point3]' = None):
        '''
        Construtor de um triângulo.

        ---

        Parâmetros:

            - vertex_1: Point3 - Primeiro vértice do triângulo.

            - vertex_2: Point3 - Segundo vértice do triângulo.

            - vertex_3: Point3 - Terceiro vértice do triângulo.

            - normals: tuple[Point3, Point3, Point3] - Tupla contendo as normais de cada vértice do triângulo. Caso não seja especificado, as normais serão calculadas automaticamente.
        '''
        self.__vertexes = np.array([vertex_1, vertex_2, vertex_3])
        
        if normals is not None:
            for i in range(len(normals)):
                normals[i] = normals[i].unit_vector()
            self.__normals = np.array(normals)
        else:
            self.__normals = None
    
    @property
    def vertexes(self) -> np.ndarray:
        '''
        Retorna um array contendo os vértices do triângulo.
        '''
        return self.__vertexes
    
    @property
    def vertex_1(self) -> Point3:
        '''
        Retorna o primeiro vértice do triângulo.
        '''
        return self.__vertexes[0]
    
    @property
    def vertex_2(self) -> Point3:
        '''
        Retorna o segundo vértice do triângulo.
        '''
        return self.__vertexes[1]
    
    @property
    def vertex_3(self) -> Point3:
        '''
        Retorna o terceiro vértice do triângulo.
        '''
        return self.__vertexes[2]
    
    @property
    def normals(self) -> Union[np.ndarray, None]:
        '''
        Retorna um array contendo as normais de cada vértice do triângulo.
        '''
        return self.__normals
    
    @property
    def normal_1(self) -> Union[Point3, None]:
        '''
        Retorna a normal do primeiro vértice do triângulo.
        '''
        return self.__normals[0] if self.__normals is not None else None
    
    @property
    def normal_2(self) -> Union[Point3, None]:
        '''
        Retorna a normal do segundo vértice do triângulo.
        '''
        return self.__normals[1] if self.__normals is not None else None
    
    @property
    def normal_3(self) -> Union[Point3, None]:
        '''
        Retorna a normal do terceiro vértice do triângulo.
        '''
        return self.__normals[2] if self.__normals is not None else None
    
    def __getitem__(self, index) -> Point3:
        '''
        Retorna o vértice especificado.

        0 = primeiro vértice, 1 = segundo vértice, 2 = terceiro vértice.
        '''
        return self.__vertexes[index]

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        '''
        Verifica se um raio atinge a triângulo.

        ---

        Parâmetros:

            - ray: Ray - Raio a ser verificado.

            - t_interval: Interval - Intervalo de t em que o raio pode atingir a triângulo.
        
        ---

        Retorno:

            - tuple[bool, HitRecord] - Tupla contendo um booleano que indica se o raio atingiu a triângulo e um registro de acerto (hit record) com informações sobre o acerto. Caso o raio não atinja a triângulo, o registro de acerto é None.
        '''
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
        
        if self.__normals is None:
            return True, HitRecord(intersect_point, normal, t, ray)
        else:
            distance_edge_1_to_intersect_point = (intersect_point - self.vertex_1).squared_length()
            distance_edge_2_to_intersect_point = (intersect_point - self.vertex_2).squared_length()
            distance_edge_3_to_intersect_point = (intersect_point - self.vertex_3).squared_length()
            normal = self.normal_1 / distance_edge_1_to_intersect_point + self.normal_2 / distance_edge_2_to_intersect_point + self.normal_3 / distance_edge_3_to_intersect_point
            normal = normal.unit_vector()
            return True, HitRecord(intersect_point, normal, t, ray)
    
    def scale(self, factor: float):
        '''
        Escala o triângulo.

        ---

        Parâmetros:

            - factor: float - Fator de escala.
        '''
        for i in range(len(self.__vertexes)):
            self.__vertexes[i] *= factor
    
    def translate(self, offset: Vec3):
        '''
        Translada o triângulo.

        ---

        Parâmetros:

            - offset: Vec3 - Vetor de translação.
        '''
        for i in range(len(self.__vertexes)):
            self.__vertexes[i] += offset