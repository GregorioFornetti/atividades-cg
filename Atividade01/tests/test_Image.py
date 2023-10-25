
import numpy as np
from Atividade01.src.Image import Image
from Atividade02.src.vectorized.Vec3 import Color

class ImageTests:

    def test_init(self):
        img = Image(2, 2)

        assert img.width == 2
        assert img.height == 2

        assert img[0, 0] == None
        assert img[0, 1] == None
        assert img[1, 0] == None
        assert img[1, 1] == None
    
    def test_set_and_get_item(self):
        img = Image(2, 2)

        img[0, 0] = Color(0.1, 0.2, 0.3)
        img[0, 1] = Color(0.4, 0.5, 0.6)
        img[1, 0] = Color(0.7, 0.8, 0.9)
        img[1, 1] = Color(1.0, 1.0, 1.0)

        assert img[0, 0] == Color(0.1, 0.2, 0.3)
        assert img[0, 1] == Color(0.4, 0.5, 0.6)
        assert img[1, 0] == Color(0.7, 0.8, 0.9)
        assert img[1, 1] == Color(1.0, 1.0, 1.0)
    
    def test_to_uint8_matrix(self):
        img = Image(2, 2)

        img[0, 0] = Color(0.1, 0.2, 0.3)
        img[0, 1] = Color(0.4, 0.5, 0.6)
        img[1, 0] = Color(0.7, 0.8, 0.9)
        img[1, 1] = Color(1.0, 1.0, 1.0)

        img_matrix = img.to_uint8_matrix()

        assert img_matrix[0, 0] == np.array([25, 51, 76])
        assert img_matrix[0, 1] == np.array([102, 127, 153])
        assert img_matrix[1, 0] == np.array([178, 204, 229])
        assert img_matrix[1, 1] == np.array([255, 255, 255])
    
    def test_is_all_pixels_set(self):
        img = Image(2, 2)

        assert img.all_pixels_set == False

        img[0, 0] = Color(0.1, 0.2, 0.3)

        assert img.all_pixels_set == False

        img[0, 1] = Color(0.4, 0.5, 0.6)

        assert img.all_pixels_set == False

        img[1, 0] = Color(0.7, 0.8, 0.9)

        assert img.all_pixels_set == False

        img[1, 1] = Color(1.0, 1.0, 1.0)

        assert img.all_pixels_set == True