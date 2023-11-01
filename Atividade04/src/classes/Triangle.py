
from Atividade02.src.vectorized.Vec3 import Point3
from Atividade04.src.classes.Hittable import Hittable
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.HitRecord import HitRecord
from Atividade04.src.classes.Interval import Interval



class Triangle(Hittable):

    def __init__(self, point1: Point3, point2: Point3, point3: Point3):
        self.__point1 = point1
        self.__point2 = point2
        self.__point3 = point3
    
    @property
    def point1(self) -> Point3:
        return self.__point1
    
    @property
    def point2(self) -> Point3:
        return self.__point2
    
    @property
    def point3(self) -> Point3:
        return self.__point3

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        # Descobrindo o vetor normal
        v1_to_v2 = self.point2 - self.point1
        v1_to_v3 = self.point3 - self.point1
        normal = v1_to_v2.cross(v1_to_v3)

        # Descobrindo o valor P: intersecção do raio com o plano formado pelo triângulo
        normal_dot_ray_dir = normal.dot(ray.direction)
        if normal_dot_ray_dir == 0:
            return False, None  # O raio é paralelo ao plano
        
        d = -normal.dot(self.point1)
        t = -(normal.dot(ray.origin) + d) / normal_dot_ray_dir

        if t not in t_interval:
            return False, None  # O triângulo está atrás do raio
        
        intersect_point = ray.at(t)

        # Verificando se o ponto de intersecção está dentro ou fora do triângulo
        # Todo lugar que retornar False, quer dizer que o ponto está à direita da aresta, logo, fora do triângulo
        # Só estará dentro do triângulo se para todas as arestas, o ponto estiver para esquerda
        edge_1 = self.point2 - self.point1
        vp1= intersect_point - self.point1
        c = edge_1.cross(vp1)
        if normal.dot(c) < 0:
            return False, None
        
        edge_2 = self.point3 - self.point2
        vp2= intersect_point - self.point2
        c = edge_2.cross(vp2)
        if normal.dot(c) < 0:
            return False, None

        edge_3 = self.point1 - self.point3
        vp3= intersect_point - self.point3
        c = edge_3.cross(vp3)
        if normal.dot(c) < 0:
            return False, None
        
        return True, HitRecord(intersect_point, normal, t, ray)