'''
Classe base para as Matrizes (Mat2, Mat3 e Mat4)
'''


from typing import Union
import numpy as np
from Atividade02.interactive.Vec import Vec


class Mat:
    """
    .. automethod:: __neg__
    .. automethod:: __getitem__
    .. automethod:: __add__
    .. automethod:: __sub__
    .. automethod:: __mul__
    .. automethod:: __truediv__
    .. automethod:: __iadd__
    .. automethod:: __isub__
    .. automethod:: __imul__
    .. automethod:: __itruediv__
    .. automethod:: __repr__
    """

    def __init__(self, matrix: Union[np.ndarray, list]):
        '''
        Construtor da classe de matrizes. Recebe uma matriz numpy (ou uma lista) que será utilizada para guardar os dados da matriz.

        --- 

        Parâmetros:

            - matrix: Union[np.ndarray, list] - Matriz numpy (ou lista) que será utilizada para guardar os dados da matriz.
        '''
        self.matrix = matrix
        if isinstance(matrix, list):
            self.matrix = np.array(matrix, dtype=np.float64)
        elif isinstance(matrix, np.ndarray) and matrix.dtype != np.float64:
            self.matrix = matrix.astype(np.float64)
        self.shape = None  # Deve ser definido nas classes filhas

    def __neg__(self) -> 'Mat':
        '''
        Inverte o sinal de todos elementos da matriz.

        ---

        Retorno:

            - Mat - Versão negativa da matriz.
        '''
        new_matrix = np.zeros(self.shape, dtype=np.float64)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                new_matrix[i,j] = -self.matrix[i,j]
        return self.__class__(new_matrix)
    
    def __getitem__(self, key) -> Union[np.float64, np.ndarray]:
        '''
        Retorna o valor (ou valores) dos indices escolhidos.

        Para mais operações de índices, veja: https://numpy.org/doc/stable/user/basics.indexing.html

        ---

        Parâmetros:
            
            - key: - Índice de acesso à matriz

        ---

        Retorno:
            
            - Union[np.ndarray, np.float64] - Valores contidos nos índices escolhidos.
        '''
        return self.matrix[key]

    def __setitem__(self, key, value):
        '''
        Atribui valores aos indices escolhidos

        ---

        Parâmetros:
            
            - key: - Índice de acesso à matriz

            - value: - Valores a serem colocado
        '''
        self.matrix[key] = value

    

    def __add__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat - Resultado da soma.

        '''
        if isinstance(other, Mat):
            # Somando duas matrizes - elemento a elemento
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] + other.matrix[i,j]
            return self.__class__(new_matrix)
        elif isinstance(other, Vec):
            # Somando uma matriz e um vetor - cada linha da matriz é somada com o vetor
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] + other.vec[j]
            return self.__class__(new_matrix)
        else:
            # Somando uma matriz e um número - cada elemento da matriz é somado com o número
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] + other
            return self.__class__(new_matrix)
    
    def __sub__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat - Resultado da subtração.
        '''
        if isinstance(other, Mat):
            # Subtraindo duas matrizes - elemento a elemento
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] - other.matrix[i,j]
            return self.__class__(new_matrix)
        elif isinstance(other, Vec):
            # Subtraindo uma matriz e um vetor - cada linha da matriz é subtraida com o vetor
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] - other.vec[j]
            return self.__class__(new_matrix)
        else:
            # Subtraindo uma matriz e um número - cada elemento da matriz é subtraido com o número
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] - other
            return self.__class__(new_matrix)
    
    def __mul__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da multiplicação.
        '''
        if isinstance(other, Mat):
            # Multiplicando duas matrizes - elemento a elemento
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] * other.matrix[i,j]
            return self.__class__(new_matrix)
        elif isinstance(other, Vec):
            # Multiplicando uma matriz e um vetor - cada linha da matriz é multiplicada com o vetor
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] * other.vec[j]
            return self.__class__(new_matrix)
        else:
            # Multiplicando uma matriz e um número - cada elemento da matriz é multiplicada com o número
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] * other
            return self.__class__(new_matrix)
    
    def __truediv__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da divisão.
        '''
        if isinstance(other, Mat):
            # Dividindo duas matrizes - elemento a elemento
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] / other.matrix[i,j]
            return self.__class__(new_matrix)
        elif isinstance(other, Vec):
            # Dividindo uma matriz e um vetor - cada linha da matriz é dividida com o vetor
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] / other.vec[j]
            return self.__class__(new_matrix)
        else:
            # Dividindo uma matriz e um número - cada elemento da matriz é dividida com o número
            new_matrix = np.zeros(self.shape, dtype=np.float64)
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    new_matrix[i,j] = self.matrix[i,j] / other
            return self.__class__(new_matrix)


    def __iadd__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Soma elemento a elemento de duas matrizes.
        
        Ou soma um número a cada elemento da matriz.

        Ou soma um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser somado.
        
        ---

        Retorno:

            - Mat - Resultado da soma.

        '''
        if isinstance(other, Mat):
            # Somando duas matrizes - elemento a elemento
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] + other.matrix[i,j]
            return self
        elif isinstance(other, Vec):
            # Somando uma matriz e um vetor - cada linha da matriz é somada com o vetor
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] + other.vec[j]
            return self
        else:
            # Somando uma matriz e um número - cada elemento da matriz é somado com o número
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] + other
            return self
    
    def __isub__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Subtrai elemento a elemento de duas matrizes.
        
        Ou subtrai um número a cada elemento da matriz.

        Ou subtrai um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser subtraido.
        
        ---

        Retorno:

            - Mat - Resultado da subtração.
        '''
        if isinstance(other, Mat):
            # Subtraindo duas matrizes - elemento a elemento
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] - other.matrix[i,j]
            return self
        elif isinstance(other, Vec):
            # Subtraindo uma matriz e um vetor - cada linha da matriz é subtraida com o vetor
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] - other.vec[j]
            return self
        else:
            # Subtraindo uma matriz e um número - cada elemento da matriz é subtraido com o número
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] - other
            return self
    
    def __imul__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Multiplica elemento a elemento de duas matrizes.
        
        Ou multiplica um número a cada elemento da matriz.

        Ou multiplica um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da multiplicação.
        '''
        if isinstance(other, Mat):
            # Multiplicando duas matrizes - elemento a elemento
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] * other.matrix[i,j]
            return self
        elif isinstance(other, Vec):
            # Multiplicando uma matriz e um vetor - cada linha da matriz é multiplicada com o vetor
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] * other.vec[j]
            return self
        else:
            # Multiplicando uma matriz e um número - cada elemento da matriz é multiplicado com o número
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] * other
            return self

    def __itruediv__(self, other: Union['Mat', Vec, np.float64]) -> 'Mat':
        '''
        Divide elemento a elemento de duas matrizes.
        
        Ou Divide um número a cada elemento da matriz.

        Ou Divide um vetor a cada linha da matriz.

        ---

        Parâmetros:

            - other: Union['Mat', Vec, np.float64] - Matriz, vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Mat - Resultado da divisão.
        '''
        if isinstance(other, Mat):
            # Dividindo duas matrizes - elemento a elemento
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] / other.matrix[i,j]
            return self
        elif isinstance(other, Vec):
            # Dividindo uma matriz e um vetor - cada linha da matriz é dividida com o vetor
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] / other.vec[j]
            return self
        else:
            # Dividindo uma matriz e um número - cada elemento da matriz é dividido com o número
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    self.matrix[i,j] = self.matrix[i,j] / other
            return self
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando a matriz.

        ---

        Retorno:
            
                - str - String representando a matriz.
        '''
        string = ""
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                string += f"{self.matrix[i,j]} "
            string = string[:-1]
            string += "\n"
        return string
    
    def dot(self, other: 'Mat') -> 'Mat':
        '''
        Retorna o resultado da multiplicação de matrizes.

        ---

        Parâmetros:

            - other: Mat - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - Mat - Resultado do produto escalar.
        '''
        new_matrix = np.zeros((self.shape[0], other.shape[1]), dtype=np.float64)
        for i in range(self.shape[0]):
            for j in range(other.shape[1]):
                for k in range(self.shape[1]):
                    new_matrix[i,j] += self.matrix[i,k] * other.matrix[k,j]
        return self.__class__(new_matrix)
