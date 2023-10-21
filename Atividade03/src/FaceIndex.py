from __future__ import annotations
from typing import Optional, Union

class TriangleFaceIndex:

    
    def __init__(self, vertex_index: int, texture_index: Optional[int] = None, normal_index: Optional[int] = None):
        '''
        Construtor da classe FaceIndex.

        Responsável por armazenar os índices de um vértice, textura e normal de uma face.

        O valor None é utilizado para indicar que algum índice não foi especificado.

        OBS: este objeto é utilizado apenas para armazenar parte dos índices de uma face. Uma face completa é representada por um objeto da classe TriangleFaceIndexes (ou um conjunto de objetos TriangleFaceIndex).

        ---

        Parâmetros:

            - vertex_index: int - Índice do vértice da face.

            - texture_index: Optional[int] - Índice da textura da face. Caso não seja especificado, o valor padrão é None.

            - normal_index: Optional[int] - Índice da normal da face. Caso não seja especificado, o valor padrão é None.
        '''
        self.__vertex_index = vertex_index
        self.__texture_index = texture_index
        self.__normal_index = normal_index
    
    @property
    def vertex_index(self):
        '''
        Retorna o índice do vértice da face.

        ---

        Retorno:

            - int - Índice do vértice da face.
        '''
        return self.__vertex_index
    
    @property
    def texture_index(self):
        '''
        Retorna o índice da textura da face.

        ---

        Retorno:

            - int - Índice da textura da face.
        '''
        return self.__texture_index
    
    @property
    def normal_index(self):
        '''
        Retorna o índice da normal da face.

        ---

        Retorno:

            - int - Índice da normal da face.
        '''
        return self.__normal_index

class TriangleFaceIndexes:

    def __init__(self, vertexes_indexes: list[int], textures_indexes: list[Union[int, None]] = None, normal_index: list[Union[int, None]] = None):
        '''
        Construtor da classe FaceIndex.

        Responsável por armazenar os índices de um vértice, textura e normal de uma face.

        O valor None é utilizado para indicar que o índice não foi especificado.

        ---

        Parâmetros:

            - vertex_index: int - Índice do vértice da face.

            - texture_index: int - Índice da textura da face.

            - normal_index: int - Índice da normal da face.
        '''
        self.__vertex_index = vertex_index
        self.__texture_index = texture_index
        self.__normal_index = normal_index
    
    @property
    def vertex_index(self):
        '''
        Retorna o índice do vértice da face.

        ---

        Retorno:

            - int - Índice do vértice da face.
        '''
        return self.__vertex_index