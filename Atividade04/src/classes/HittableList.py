
from Atividade04.src.classes.Hittable import Hittable
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.HitRecord import HitRecord
from Atividade04.src.classes.Interval import Interval


class HittableList:
    
    def __init__(self):
        self.objects: list[Hittable] = []
    
    def add(self, obj: Hittable):
        self.objects.append(obj)
    
    def clear(self):
        self.objects.clear()
    
    def hit(self, ray: Ray, interval: Interval) -> "tuple[bool, HitRecord]":
        hit_anything = False
        closest_so_far = interval.max
        for obj in self.objects:
            hit, rec = obj.hit(ray, Interval(interval.min, closest_so_far))
            if hit:
                hit_anything = True
                closest_so_far = rec.t
                hit_record = rec
        
        if hit_anything:
            return True, hit_record
        else:
            return False, None