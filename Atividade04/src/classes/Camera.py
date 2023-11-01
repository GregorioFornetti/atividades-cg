
from Atividade01.src.Image import Image
from Atividade01.src.ImageIO import ImageWriter
from Atividade02.src.vectorized.Vec3 import Vec3, Point3, Color
from Atividade04.src.classes.HittableList import HittableList
from Atividade04.src.classes.Ray import Ray
from Atividade04.src.classes.Interval import Interval
from Atividade04.src.constants import infinity

from IPython.display import display
from tqdm import tqdm


class Camera:

    def initialize(self):
        self.aspect_ratio = 16.0 / 9.0
        self.image_width = 400

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

    def ray_color(self, ray: Ray, world: HittableList) -> Color:
        hit, rec = world.hit(ray, Interval(0, infinity))
        if hit:
            return Color((0.5 * (rec.normal + Color([1, 1, 1]))).vec)
        
        unit_direction = ray.direction.unit_vector()
        t = 0.5 * (unit_direction.y + 1.0)
        return (1.0 - t) * Color([1.0, 1.0, 1.0]) + t * Color([0.5, 0.7, 1.0])
    
    def render(self, world: HittableList, filename: str) -> Image:
        self.initialize()

        image = Image(self.image_width, self.image_height)
        for j in tqdm(range(self.image_height)):
            for i in range(self.image_width):
                self.pixel_center = self.pixel00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
                self.ray_direction = self.pixel_center - self.camera_center
                ray = Ray(self.camera_center, self.ray_direction)

                pixel_color = self.ray_color(ray, world)
                image[j, i] = pixel_color

        img_writer = ImageWriter(image)
        img_writer.save(filename)
        display(img_writer.image)
        
        return image