'''
Testes unitários para a classes de ImageIO: ImageReader e ImageWriter.
'''

from Atividade01.src.ImageIO import ImageReader, ImageWriter
from Atividade01.src.Image import Image
from Atividade02.src.vectorized.Vec3 import Color

import numpy as np
import os
import pytest

test_folder = "images_test"

def clean_test_images_folder():
    if not os.path.exists(test_folder):
        os.mkdir(test_folder)
    else:
        for file in os.listdir(test_folder):
            os.remove(f"{test_folder}/" + file)


class TestImageIO:

    def read_write_test(self, img_matrix, save_path):
        '''
        Testa se é possível salvar a imagem e ler ela de volta ao mesmo formato.
        '''
        img_writer = ImageWriter(img_matrix)

        img_writer.save(save_path)

        assert os.path.isfile(save_path)  # Verifica se o arquivo foi salvo

        img_reader = ImageReader()

        img_matrix_read = img_reader.read_as_uint8_matrix(save_path)
        assert np.array_equal(img_matrix, img_matrix_read)  # Verifica se a imagem lida é igual a imagem salva (formato 0 a 255, uint8)

        img_matrix_read = img_reader.read_as_float_matrix(save_path)
        assert np.array_equal(img_matrix.astype(float) / 255, img_matrix_read)  # Verifica se a imagem lida é igual a imagem salva (formato 0 a 1, float)


    def test_saving_and_reading_degrade(self):
        '''
        Testa se é possível salvar a imagem de degradê e ler ela de volta ao mesmo formato.
        '''
        clean_test_images_folder()

        # Tamanho da imagem
        img_width = 256
        img_height = 256

        # Cores do degradê (RGB)
        top_color = np.array([0, 0, 255])
        bottom_color = np.array([255, 0, 0])

        img_matrix = np.zeros((img_height, img_width, 3), dtype=np.uint8)

        for i in range(img_height):
            # A imagem começa de cima para baixo
            # O percentual da cor de cima vai diminundo conforme o decorrer das iterações, enquanto a cor de baixo vai aumentando
            img_matrix[i] += (bottom_color * (i / img_height)).astype(np.uint8)
            img_matrix[i] += (top_color * (1 - i / img_height)).astype(np.uint8)

        self.read_write_test(img_matrix, f"{test_folder}/degrade.png")

        clean_test_images_folder()

    def test_saving_and_reading_circle(self):
        '''
        Testa se é possível salvar a imagem de um círculo e ler ela de volta ao mesmo formato.
        '''
        clean_test_images_folder()
        # Baseado em: https://stackoverflow.com/questions/17163636/filled-circle-in-matrix2d-array

        # Tamanho da imagem
        img_width = 256
        img_height = 256

        # Configurações do círculo
        circle_center_x = img_width // 2
        circle_center_y = img_height // 2
        radius = 100
        circle_color = np.array([255, 0, 0])

        img_matrix = np.zeros((img_height, img_width, 3), dtype=np.uint8)

        for i in range(img_height):
            for j in range(img_width):
                if (j - circle_center_x) ** 2 + (i - circle_center_y) ** 2 <= radius ** 2:
                    img_matrix[i][j] = circle_color
        
        self.read_write_test(img_matrix, f"{test_folder}/circle.png")

        clean_test_images_folder()
    
    def test_saving_and_reading_square(self):
        '''
        Testa se é possível salvar a imagem de um quadrado e ler ela de volta ao mesmo formato.
        '''
        clean_test_images_folder()

        # Tamanho da imagem
        img_width = 256
        img_height = 256

        # Configurações do quadrado
        square_center_x = img_width // 2
        square_center_y = img_height // 2
        square_size = 200
        square_color = np.array([255, 0, 0])

        img_matrix = np.zeros((img_height, img_width, 3), dtype=np.uint8)

        for i in range(img_height):
            for j in range(img_width):
                if abs(j - square_center_x) <= square_size // 2 and abs(i - square_center_y) <= square_size // 2:
                    img_matrix[i][j] = square_color
        
        self.read_write_test(img_matrix, f"{test_folder}/square.png")

        clean_test_images_folder()
    
    def test_save_image_with_custom_image_obj(self):
        clean_test_images_folder()

        img = Image(2, 2)

        with pytest.raises(ValueError):  # ainda não foi definido nenhum pixel
            ImageWriter(img)
        
        img[0, 0] = Color([0.1, 0.2, 0.3])
        img[0, 1] = Color([0.4, 0.5, 0.6])
        img[1, 0] = Color([0.7, 0.8, 0.9])
        img[1, 1] = Color([1.0, 1.0, 1.0])

        img_writer = ImageWriter(img)

        self.read_write_test(img.to_uint8_matrix(), f"{test_folder}/custom_image_obj.png")

        clean_test_images_folder()