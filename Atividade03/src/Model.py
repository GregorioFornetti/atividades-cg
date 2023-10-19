
from Atividade02.src.vectorized.Vec3 import Vec3
import numpy as np

class Model:

    def __init__(self):
        pass

    def read_from_obj_file(self, file_path: str):
        self.__vertexes = []
        self.__faces = []

        with open(file_path, 'r') as file:
            for line in file:
                if line.startswith('v '):
                    current_vertex_coordinates = [float(coordinate) for coordinate in line.split()[1:]]

                    if len(current_vertex_coordinates) == 3:
                        self.__vertexes.append(Vec3(current_vertex_coordinates))
                    else:
                        self.__vertexes.append(Vec3(current_vertex_coordinates[:-1]))
                
                elif line.startswith('f '):
                    pass