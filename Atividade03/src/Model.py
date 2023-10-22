
from Atividade02.src.vectorized.Vec3 import Vec3
from Atividade03.src.Triangle import Triangle
from Atividade03.src.TriangleFaceIndexes import TriangleFaceIndexes
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
        self.__faces_indexes: list[TriangleFaceIndexes] = []

        with open(file_path, 'r') as file:
            for line_num, line in enumerate(file):
                if line.startswith('v '):
                    # Lendo novos vértices
                    
                    line_values_str = line.replace('v ', '')
                    current_vertex_coordinates = [float(coordinate) for coordinate in line_values_str.split()]

                    if len(current_vertex_coordinates) == 3:
                        self.__vertexes.append(Vec3(current_vertex_coordinates))
                    elif len(current_vertex_coordinates) == 4:
                        self.__vertexes.append(Vec3(current_vertex_coordinates[:-1]))  # A ultima coordenada é ignorada
                    else:
                        raise ValueError(f'Modelo com número de coordenadas inválido para um vértice: {len(current_vertex_coordinates)}. Deve ser apenas 3 ou 4.\nO erro ocorreu na linha {line_num + 1}:\n{line}')
                
                elif line.startswith('f '):
                    # Lendo novas faces

                    line_values_str = line.replace('f ', '')
                    current_faces_str = line_values_str.split()

                    if len(current_faces_str) != 3:
                        raise ValueError(f'Modelo com número de faces inválido: {len(current_faces_str)}. Deve ser apenas 3.\nO erro ocorreu na linha {line_num + 1}:\n{line}')
                    
                    vertexes_indexes = []
                    textures_indexes = []
                    normals_indexes = []

                    for face_str in current_faces_str:
                        current_face_index = [int(index) - 1 if index != '' else None for index in face_str.split('/')]

                        if len(current_face_index) == 1:
                            # Apenas os índices dos vértices foram especificados
                            vertexes_indexes.append(current_face_index[0])
                            textures_indexes.append(None)
                            normals_indexes.append(None)
                        
                        elif len(current_face_index) == 2:
                            # Os índices dos vértices e das texturas foram especificados
                            vertexes_indexes.append(current_face_index[0])
                            textures_indexes.append(current_face_index[1])
                            normals_indexes.append(None)
                        
                        elif len(current_face_index) == 3:
                            # Os índices dos vértices, das texturas (talvez não, mas já vai estar None) e das normais foram especificados
                            vertexes_indexes.append(current_face_index[0])
                            textures_indexes.append(current_face_index[1])
                            normals_indexes.append(current_face_index[2])

                        else:
                            raise ValueError(f'Modelo com número de índices inválido para uma face: {len(current_face_index)}. Deve ser apenas 1, 2 ou 3.\nO erro ocorreu na linha {line_num + 1}:\n{line}')

                    current_face_indexes = TriangleFaceIndexes(vertexes_indexes, textures_indexes, normals_indexes)
                    self.__faces_indexes.append(TriangleFaceIndexes(vertexes_indexes, textures_indexes, normals_indexes))
                    try:
                        self.__faces.append(Triangle(self.__vertexes[current_face_indexes[0][0]], self.__vertexes[current_face_indexes[0][1]], self.__vertexes[current_face_indexes[0][2]]))
                    except Exception as e:
                        raise ValueError(f'Erro ao criar face com os índices especificados (algum índice de vértice é maior que o número de vértices). O erro ocorreu na linha {line_num + 1}:\n{line}') from e
    
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
    
    @property
    def faces_indexes(self):
        '''
        Retorna os índices das faces do modelo.

        ---

        Retorno:

            - list[TriangleFaceIndexes] - Lista de índices das faces do modelo.
        '''
        return self.__faces_indexes
