
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.HitRecord import HitRecord
from Atividade04.src.classes.Interval import Interval


class Hittable:

    def hit(self, ray: Ray, t_interval: Interval) -> "tuple[bool, HitRecord]":
        raise NotImplementedError('Esse método método deve ser implementado na classe filha.')