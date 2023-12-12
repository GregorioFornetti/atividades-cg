from Atividade02.src.vectorized.Vec3 import Vec3, Color
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes import HitRecord
from Atividade06.src.Material import Material

class Metal(Material):
    
    def __init__(self, albedo: Color, fuzz: float = 0.0):
        self.albedo = albedo
        self.fuzz = fuzz if fuzz < 1 else 1
    
    def scatter(self, ray: Ray, rec: HitRecord) -> 'tuple[bool, Ray, Color]':
        reflected = Vec3.reflect(ray.direction.unit_vector(), rec.normal)
        scattered = Ray(rec.p, reflected + self.fuzz * Vec3.random_in_unit_sphere())
        attenuation = self.albedo
        return scattered.direction.dot(rec.normal) > 0, scattered, attenuation