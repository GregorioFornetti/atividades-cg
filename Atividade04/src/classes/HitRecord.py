from Atividade02.src.vectorized.Vec3 import Vec3, Point3
from Atividade04.src.classes.Ray import Ray

class HitRecord:

    def __init__(self, p: Point3, normal: Vec3, t: float, ray: Ray):
        self.__p = p
        self.__t = t
        self.set_normal(normal, ray)
    
    def set_normal(self, outward_normal: Vec3, ray: Ray):
        self.__front_face = ray.direction.dot(outward_normal) < 0
        self.__normal = outward_normal if self.front_face else -outward_normal
    
    @property
    def p(self):
        return self.__p
    
    @property
    def normal(self):
        return self.__normal
    
    @property
    def t(self):
        return self.__t
    
    @property
    def front_face(self):
        return self.__front_face