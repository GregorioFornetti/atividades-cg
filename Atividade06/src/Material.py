from Atividade02.src.vectorized.Vec3 import Color
from Atividade04.src.classes.HitRecord import HitRecord
from Atividade04.src.classes.Ray import Ray

class Material:
    def scatter(self, ray: Ray, rec: HitRecord) -> 'tuple[bool, Ray, Color]':
        raise NotImplementedError