from Atividade02.src.vectorized.Vec3 import Color
from Atividade04.src.classes.Ray import Ray

class Material:
    def scatter(self, ray: Ray, rec) -> 'tuple[bool, Ray, Color]':
        raise NotImplementedError