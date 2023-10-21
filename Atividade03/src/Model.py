
from Atividade02.src.vectorized.Vec3 import Vec3
from Atividade03.src.Triangle import Triangle
from Atividade03.src.FaceIndex import FaceIndex
import numpy as np

class Model:

    def __init__(self, file_path: str):
        '''
        Construtor da classe Model. Recebe o caminho do arquivo .obj e o lê, armazenando os vértices e faces do modelo.

        Atualmente, o modelo só suporta faces com 3 vértices (triângulos), gerando erro caso o arquivo .obj contenha faces com mais de 3 vértices.

        Ainda não há suporte para faces com texturas ou normais (elas são ignoradas, não gerando erro caso o arquivo .obj contenha essas informações).

        ---

        Parâmetros:

            - file_path: str - Caminho do arquivo .obj a ser lido.
        '''
        self.__vertexes: list[Vec3] = []
        self.__faces: list[Triangle] = []
        self.__faces_indexes: list[list[FaceIndex]] = []

        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    # Lendo novos vértices

                    line = line.replace('v ', '')
                    current_vertex_coordinates = [float(coordinate) for coordinate in line.split()]

                    if len(current_vertex_coordinates) == 3:
                        self.__vertexes.append(Vec3(current_vertex_coordinates))
                    else:
                        self.__vertexes.append(Vec3(current_vertex_coordinates[:-1]))  # A ultima coordenada é ignorada
                
                elif line.startswith('f '):
                    # Lendo novas faces

                    line = line.replace('f ', '')
                    current_faces_str = line.split()
                    current_face_indexes: list[FaceIndex] = []

                    for face_str in current_faces_str:
                        current_face_index = [int(index) - 1 if index != '' else None for index in face_str.split('/')]
                        current_face_index = FaceIndex(*current_face_index)
                        current_face_indexes.append(current_face_index)

                    if len(current_face_indexes) > 3:  # Atualmente, o modelo só suporta faces com 3 vértices (triângulos)
                        raise Exception('Modelo não suporta faces com mais de 3 vértices')
                    
                    self.__faces_indexes.append(current_face_indexes)
                    self.__faces.append(Triangle(self.__vertexes[current_face_indexes[0].vertex_index], self.__vertexes[current_face_indexes[1].vertex_index], self.__vertexes[current_face_indexes[2].vertex_index]))
    
    @property
    def vertexes(self):
        '''
        Retorna os vértices do modelo.

        ---

        Retorno:

            - list[Vec3] - Lista de vértices do modelo.
        '''
        return self.__vertexes
    
    @property
    def faces(self):
        '''
        Retorna as faces do modelo.

        Atualmente, cada triângulo é representado apenas pelos seus vértices, sem informações de textura ou normais.

        ---

        Retorno:

            - list[Triangle] - Lista de faces do modelo.
        '''
        return self.__faces
