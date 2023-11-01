
from Atividade02.src.vectorized.Vec3 import Point3
from Atividade04.src.classes.Hittable import Hittable
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.HitRecord import HitRecord
from Atividade04.src.classes.Interval import Interval

import numpy as np


class Sphere(Hittable):

    def __init__(self, center: Point3, radius: float):
        self.__center = center
        self.__radius = radius
    
    @property
    def center(self):
        return self.__center
    
    @property
    def radius(self):
        return self.__radius

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        oc = ray.origin - self.center
        a = ray.direction.squared_length()
        half_b = oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius ** 2

        discriminant = half_b ** 2 - a * c

        if discriminant < 0:
            return False, None
        else:
            root = np.sqrt(discriminant)
            t = (-half_b - root) / a
            if t not in t_interval:
                t = (-half_b + root) / a
                if t not in t_interval:
                    return False, None
            
            p = ray.at(t)
            normal = (p - self.center) / self.radius
            return True, HitRecord(p, normal, t, ray)