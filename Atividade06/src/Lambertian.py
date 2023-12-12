
from Atividade02.src.vectorized.Vec3 import Vec3, Color
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes import HitRecord
from Atividade06.src.Material import Material


class Lambertian(Material):

    def __init__(self, albedo: Color):
        self.albedo = albedo
    
    def scatter(self, ray: Ray, rec: HitRecord) -> 'tuple[bool, Ray, Color]':
        direction: Vec3 = rec.normal + Vec3.random_unit_vector()
        if direction.near_zero():
            direction = rec.normal
        
        scattered = Ray(rec.p, direction)
        attenuation = self.albedo
        return True, scattered, attenuation