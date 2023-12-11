
from Atividade01.src.Image import Image
from Atividade01.src.ImageIO import ImageWriter
from Atividade02.src.vectorized.Vec3 import Vec3, Point3, Color
from Atividade04.src.classes.HittableList import HittableList
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.Interval import Interval
from Atividade04.src.constants import infinity
from Atividade04.src.utils import random_double

from IPython.display import display
from tqdm import tqdm
from typing import Optional


from math import sqrt

def linear_to_gamma(linear_component: float) -> float:
    return sqrt(linear_component)

def transform_color(pixel_color: Color, samples_per_pixel: int) -> Color:
    r = pixel_color.x
    g = pixel_color.y
    b = pixel_color.z

    scale = 1.0 / samples_per_pixel
    r *= scale
    g *= scale
    b *= scale

    r = linear_to_gamma(r)
    g = linear_to_gamma(g)
    b = linear_to_gamma(b)

    intensity = Interval(0.000, 0.999)

    return Color([intensity.clamp(r), intensity.clamp(g), intensity.clamp(b)])


class Camera:

    def __init__(self, image_width: int = 400, samples_per_pixel: int = 100, max_depth: int = 10):
        self.image_width = image_width
        self.samples_per_pixel = samples_per_pixel
        self.max_depth = max_depth

    def initialize(self):
        self.aspect_ratio = 16.0 / 9.0

        self.image_height = int(self.image_width / self.aspect_ratio)
        if self.image_height < 1:
            self.image_height = 1

        self.viewport_height = 2.0
        self.viewport_width = self.viewport_height * (self.image_width / self.image_height)
        self.focal_length = 1.0
        self.camera_center = Point3([0, 0, 0])

        self.viewport_u = Vec3([self.viewport_width, 0, 0])
        self.viewport_v = Vec3([0, -self.viewport_height, 0])

        self.pixel_delta_u = self.viewport_u / self.image_width
        self.pixel_delta_v = self.viewport_v / self.image_height

        # If pixels are spaced the same distance horizontally as they are vertically, the viewport that bounds them will have the same aspect ratio as the rendered image.
        # Como estamos definindo o viewport para ter o mesmo aspect ratio da imagem (quantidade de pixels), então, os pixels terão o mesmo espaçamento horizontal e vertical.

        self.viewport_upper_left = self.camera_center - Vec3([0, 0, self.focal_length]) - (self.viewport_u / 2) - (self.viewport_v / 2)
        self.pixel00_loc = self.viewport_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)
        # Precisa adicionar 0,5 da distancia de separação dos pixels. O canto esquerdo do viewport não é o mesmo que o ponto 0,0 da imagem. O viewport precisa ter uma borda de 0,5 espaçamento de pixel para cada lado.

    def ray_color(self, ray: Ray, depth: int, world: HittableList) -> Color:
        if depth <= 0:
            return Color([0, 0, 0])

        hit, rec = world.hit(ray, Interval(0.001, infinity))
        if hit:
            direction = rec.normal + Vec3.random_unit_vector()
            return 0.5 * self.ray_color(Ray(rec.p, direction), depth - 1, world)
        
        unit_direction = ray.direction.unit_vector()
        t = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - t) * Color([1.0, 1.0, 1.0]) + t * Color([0.5, 0.7, 1.0])
    
    def render(self, world: HittableList, filename: str) -> Image:
        self.initialize()

        image = Image(self.image_width, self.image_height)
        for j in tqdm(range(self.image_height)):
            for i in range(self.image_width):
                # MUDOU AQUI
                pixel_color = Color([0, 0, 0])
                for _ in range(self.samples_per_pixel):
                    ray = self.get_ray(i, j)
                    pixel_color += self.ray_color(ray, self.max_depth, world)
                image[j, i] = transform_color(pixel_color, self.samples_per_pixel)

        img_writer = ImageWriter(image)
        img_writer.save(filename)
        display(img_writer.image)
        
        return image

    # NOVO MÉTODO
    def get_ray(self, i: int, j: int) -> Ray:
        pixel_center = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
        pixel_sample = pixel_center + self.pixel_sample_square()
        
        return Ray(self.camera_center, pixel_sample - self.camera_center)

    #NOVO MÉTODO
    def pixel_sample_square(self) -> Vec3:
        px = -0.5 + random_double()
        py = -0.5 + random_double()
        return (px * self.pixel_delta_u) + (py * self.pixel_delta_v)