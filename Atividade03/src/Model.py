
from Atividade02.src.vectorized.Vec3 import Vec3
from Atividade03.src.Triangle import Triangle
from Atividade03.src.FaceIndex import FaceIndex
import numpy as np

class Model:

    def __init__(self):
        pass

    def read_from_obj_file(self, file_path: str):
        self.__vertexes: list[Vec3] = []
        self.__faces: list[Triangle] = []
        self.__faces_indexes: list[list[FaceIndex]] = []

        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    line = line.replace('v ', '')
                    current_vertex_coordinates = [float(coordinate) for coordinate in line.split()]

                    if len(current_vertex_coordinates) == 3:
                        self.__vertexes.append(Vec3(current_vertex_coordinates))
                    else:
                        self.__vertexes.append(Vec3(current_vertex_coordinates[:-1]))
                
                elif line.startswith('f '):
                    line = line.replace('f ', '')
                    current_faces_str = line.split()
                    current_face_indexes: list[FaceIndex] = []

                    for face_str in current_faces_str:
                        current_face_index = [int(index) - 1 for index in face_str.split('/')]
                        current_face_index = FaceIndex(current_face_index[0], current_face_index[1], current_face_index[2])
                        current_face_indexes.append(current_face_index)

                    self.__faces_indexes.append(current_face_indexes)
                    self.__faces.append(Triangle(self.__vertexes[current_face_indexes[0].vertex_index], self.__vertexes[current_face_indexes[1].vertex_index], self.__vertexes[current_face_indexes[2].vertex_index]))
