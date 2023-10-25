
import numpy as np
from Atividade02.src.vectorized.Vec3 import Color


class Image:

    def __init__(self, width: int, height: int):
        '''
        Construtor da classe Image. Cria uma matriz de pixels com as dimensões passadas como parâmetro.

        ---

        Parâmetros:

            - width: int - Largura da imagem em pixels.

            - height: int - Altura da imagem em pixels.
        '''
        self.img_matrix = np.empty((height, width), dtype=Color)
    
    def to_uint8_matrix(self) -> np.ndarray:
        '''
        Retorna uma matriz numpy representando a imagem.

        ---

        Retorno:

            - np.ndarray - Matriz numpy representando a imagem. A matriz possui valores entre 0 e 255 e é do tipo uint8.
        '''
        img_matrix = np.empty((*self.img_matrix.shape, 3), dtype=np.uint8)
        for i in range(self.img_matrix.shape[0]):
            for j in range(self.img_matrix.shape[1]):
                img_matrix[i, j, 0] = int(255.999 * self.img_matrix[i, j].r)
                img_matrix[i, j, 1] = int(255.999 * self.img_matrix[i, j].g)
                img_matrix[i, j, 2] = int(255.999 * self.img_matrix[i, j].b)
        return img_matrix
    
    def __setitem__(self, key, value: Color):
        '''
        Define o valor de um pixel da imagem. O valor de cada cor do pixel deve ser um float entre 0 e 1 !

        Exemplo:
            
        >>> img = Image(10, 10)
        >>> img[0, 0] = Color(1, 1, 1)  # Define o pixel (0, 0) como branco. 0, 0 é o canto superior esquerdo da imagem.
        >>> img[9, 9] = Color(1, 1, 1)  # Define o pixel (9, 9) como branco. 9, 9 é o canto inferior direito da imagem.

        ---

        Parâmetros:

            - key: As coordenadas do pixel.

            - value: Color - Cor do pixel.
        '''
        self.img_matrix[key] = value
    
    def __getitem__(self, key):
        '''
        Retorna o valor de um pixel da imagem.

        Exemplo:

        >>> img = Image(10, 10)
        >>> img[0, 0] = Color(1, 1, 1)
        >>> img[0, 0]  # Retorna o valor do pixel (0, 0). Canto superior esquerdo da imagem.
        Color(1, 1, 1)

        ---

        Parâmetros:

            - key: As coordenadas do pixel.

        ---

        Retorno:

            - Color - Cor do pixel.
        '''
        return self.img_matrix[key]
