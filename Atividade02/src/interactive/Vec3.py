
from typing import Union
import numpy as np
from Atividade02.src.interactive.Vec import Vec


class Vec3(Vec):
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

    def __init__(self, x: np.float64 = 0.0, y: np.float64 = 0.0, z: np.float64 = 0.0):
        '''
        Construtor da classe Vec3. Recebe as coordenadas x, y e z do vetor.

        --- 

        Parâmetros:

            - x: np.float64 = 0.0 - Coordenada x do vetor.

            - y: np.float64 = 0.0 - Coordenada y do vetor.

            - z: np.float64 = 0.0 - Coordenada z do vetor.
        '''
        if not isinstance(x, np.float64) and not isinstance(x, float) and not isinstance(x, int):
            raise TypeError(f"x precisa ser um número. Tipo recebido: {type(x)}")
        if not isinstance(y, np.float64) and not isinstance(y, float) and not isinstance(y, int):
            raise TypeError(f"y precisa ser um número. Tipo recebido: {type(y)}")
        if not isinstance(z, np.float64) and not isinstance(z, float) and not isinstance(z, int):
            raise TypeError(f"z precisa ser um número. Tipo recebido: {type(z)}")
        
        self.vec = np.array([x, y, z], dtype=np.float64)
    
    @property
    def x(self) -> np.float64:
        '''
        Coordenada x do vetor.
        '''
        return self.vec[0]
    
    @x.setter
    def x(self, value: np.float64):
        self.vec[0] = value
    
    @property
    def y(self) -> np.float64:
        '''
        Coordenada y do vetor.
        '''
        return self.vec[1]
    
    @y.setter
    def y(self, value: np.float64):
        self.vec[1] = value

    @property
    def z(self) -> np.float64:
        '''
        Coordenada z do vetor.
        '''
        return self.vec[2]

    @z.setter
    def z(self, value: np.float64):
        self.vec[2] = value
    

    def __neg__(self) -> 'Vec3':
        '''
        Inverte o sinal de todas as coordenadas do vetor.

        Exemplo:

        >>> v = Vec3(1, 2, 3)
        >>> print(-v)
        -1.0 -2.0 -3.0

        ---

        Retorno:

            - Vec3 - Versão negativa do vetor.
        '''
        return Vec3(-self.vec[0], -self.vec[1], -self.vec[2])
    
    def __getitem__(self, key: int) -> np.float64:
        '''
        Retorna a coordenada do vetor de acordo com o índice.

        Exemplo:

        >>> v = Vec3(1, 2, 3)
        >>> print(v[0])
        1.0

        ---

        Parâmetros:
            
            - key: int - Índice da coordenada do vetor (0 = x, y = 1 e z = 2).

        ---

        Retorno:
            
            - np.float64 - Valor da coordenada escolhida.
        '''
        return self.vec[key]
    

    def __add__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> print(v1 + v2)
        5.0 7.0 9.0

        Somando um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> print(v1 + 1)
        2.0 3.0 4.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec3 - Resultado da soma.

        '''
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] + other.vec[0], self.vec[1] + other.vec[1], self.vec[2] + other.vec[2])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec3(self.vec[0] + other, self.vec[1] + other, self.vec[2] + other)
        else:
            return NotImplemented  # força a chamada do método __radd__ do outro objeto, que pode estar implementado

    def __radd__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        return self.__add__(other)
    
    def __sub__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> print(v1 - v2)
        -3.0 -3.0 -3.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> print(v1 - 1)
        0.0 1.0 2.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser subtraído.

        ---

        Retorno:
            
                - Vec3 - Resultado da subtração.
        
        '''
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] - other.vec[0], self.vec[1] - other.vec[1], self.vec[2] - other.vec[2])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec3(self.vec[0] - other, self.vec[1] - other, self.vec[2] - other)
        else:
            return NotImplemented  # força a chamada do método __rsub__ do outro objeto, que pode estar implementado
    
    def __rsub__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        # A ordem importa, pois a subtração não é comutativa
        # EX: 1 / vec != vec / 1
        if isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec3(other - self.vec[0], other - self.vec[1], other - self.vec[2])
        else:
            return self.__sub__(other)
    
    def __mul__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> print(v1 * v2)
        4.0 10.0 18.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> print(v1 * 2)
        2.0 4.0 6.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec3 - Resultado da multiplicação.
        '''
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] * other.vec[0], self.vec[1] * other.vec[1], self.vec[2] * other.vec[2])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec3(self.vec[0] * other, self.vec[1] * other, self.vec[2] * other)
        else:
            return NotImplemented  # força a chamada do método __rmul__ do outro objeto, que pode estar implementado
    
    def __rmul__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        return self.__mul__(other)
    
    def __truediv__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> print(v1 / v2)
        0.25 0.4 0.5

        Dividindo um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> print(v1 / 2)
        0.5 1.0 1.5

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser utilizado como divisor.

        ---

        Retorno:

            - Vec3 - Resultado da divisão.
        '''
        if isinstance(other, Vec3):
            return Vec3(self.vec[0] / other.vec[0], self.vec[1] / other.vec[1], self.vec[2] / other.vec[2])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec3(self.vec[0] / other, self.vec[1] / other, self.vec[2] / other)
        else:
            return NotImplemented  # força a chamada do método __rtruediv__ do outro objeto, que pode estar implementado
    
    def __rtruediv__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        # A ordem importa, pois a divisão não é comutativa
        # EX: 1 / vec != vec / 1
        if isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec3(other / self.vec[0], other / self.vec[1], other / self.vec[2])
        else:
            return self.__truediv__(other)

    def __iadd__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> v1 += v2
        >>> print(v1)
        5.0 7.0 9.0

        Somando um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> v1 += 1
        >>> print(v1)
        2.0 3.0 4.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec3 - Resultado da soma.
        '''
        if isinstance(other, Vec3):
            self.vec[0] += other.vec[0]
            self.vec[1] += other.vec[1]
            self.vec[2] += other.vec[2]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] += other
            self.vec[1] += other
            self.vec[2] += other
        else:
            return NotImplemented
        return self
    
    def __isub__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> v1 -= v2
        >>> print(v1)
        -3.0 -3.0 -3.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> v1 -= 1
        >>> print(v1)
        0.0 1.0 2.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser subtraído.
        
        ---

        Retorno:

            - Vec3 - Resultado da subtração.
        '''
        if isinstance(other, Vec3):
            self.vec[0] -= other.vec[0]
            self.vec[1] -= other.vec[1]
            self.vec[2] -= other.vec[2]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] -= other
            self.vec[1] -= other
            self.vec[2] -= other
        else:
            return NotImplemented
        return self
    
    def __imul__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> v1 *= v2
        >>> print(v1)
        4.0 10.0 18.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> v1 *= 2
        >>> print(v1)
        2.0 4.0 6.0

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec3 - Resultado da multiplicação.
        '''
        if isinstance(other, Vec3):
            self.vec[0] *= other.vec[0]
            self.vec[1] *= other.vec[1]
            self.vec[2] *= other.vec[2]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] *= other
            self.vec[1] *= other
            self.vec[2] *= other
        else:
            return NotImplemented
        
        return self

    def __itruediv__(self, other: Union['Vec3', np.float64]) -> 'Vec3':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> v1 /= v2
        >>> print(v1)
        0.25 0.4 0.5

        Dividindo um vetor e um número:

        >>> v1 = Vec3(1, 2, 3)
        >>> v1 /= 2
        >>> print(v1)
        0.5 1.0 1.5

        ---

        Parâmetros:

            - other: Union['Vec3', np.float64] - Vetor ou número a ser dividido.
        
        ---

        Retorno:

            - Vec3 - Resultado da divisão.
        '''
        if isinstance(other, Vec3):
            self.vec[0] /= other.vec[0]
            self.vec[1] /= other.vec[1]
            self.vec[2] /= other.vec[2]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] /= other
            self.vec[1] /= other
            self.vec[2] /= other
        else:
            return NotImplemented
        return self
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando o vetor.

        A string é composta pelas coordenadas x, y e z do vetor, separadas por um espaço.

        Exemplo:

        >>> v = Vec3(1, 2, 3)
        >>> print(v)
        1.0 2.0 3.0
        '''
        return f"{self.vec[0]} {self.vec[1]} {self.vec[2]}"
    
    
    def length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor.

        Exemplo:

        >>> v = Vec3(1, 2, 3)
        >>> print(v.length())  # sqrt(1 ** 2 + 2 ** 2 + 3 ** 2)
        3.7416573867739413
        '''
        return np.sqrt(self.squared_length())
    
    def squared_length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor ao quadrado.

        Exemplo:

        >>> v = Vec3(1, 2, 3)
        >>> print(v.squared_length())  # 1 ** 2 + 2 ** 2 + 3 ** 2
        14.0
        '''
        return self.vec[0] ** 2 + self.vec[1] ** 2 + self.vec[2] ** 2
    
    def dot(self, other: 'Vec3') -> np.float64:
        '''
        Retorna o produto escalar entre dois vetores.

        Exemplo:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> print(v1.dot(v2))
        32.0

        ---

        Parâmetros:

            - other: 'Vec3' - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - np.float64 - Resultado do produto escalar.
        '''
        if not isinstance(other, Vec3):
            raise TypeError(f"Tipo inválido para produto escalar, esperado: Vec3, recebido: {type(other)}")
        
        return self.vec[0] * other.vec[0] + self.vec[1] * other.vec[1] + self.vec[2] * other.vec[2]
    
    def cross(self, other: 'Vec3') -> 'Vec3':
        '''
        Retorna o produto vetorial entre dois vetores.

        Exemplo:

        >>> v1 = Vec3(1, 2, 3)
        >>> v2 = Vec3(4, 5, 6)
        >>> print(v1.cross(v2))
        -3.0 6.0 -3.0

        ---

        Parâmetros:

            - other: 'Vec3' - Segundo vetor do produto vetorial.
        
        ---

        Retorno:

            - Vec3 - Resultado do produto vetorial.
        '''
        if not isinstance(other, Vec3):
            raise TypeError(f"Tipo inválido para produto vetorial, esperado: Vec3, recebido: {type(other)}")
        
        return Vec3(self.vec[1] * other.vec[2] - self.vec[2] * other.vec[1],
                    self.vec[2] * other.vec[0] - self.vec[0] * other.vec[2],
                    self.vec[0] * other.vec[1] - self.vec[1] * other.vec[0])
    
    def unit_vector(self) -> 'Vec3':
        '''
        Retorna o vetor unitário.

        Exemplo:

        >>> v = Vec3(1, 2, 3)
        >>> print(v.unit_vector())
        0.27 0.53 0.80

        ---

        Retorno:

            - Vec3 - Vetor unitário.
        '''
        return self / self.length()

Point3 = Vec3

class Color(Vec3):

    @property
    def r(self) -> np.float64:
        return self.vec[0]

    @property
    def g(self) -> np.float64:
        return self.vec[1]
    
    @property
    def b(self) -> np.float64:
        return self.vec[2]

    def __repr__(self):
        return f"{int(255.999 * self.vec[0])} {int(255.999 * self.vec[1])} {int(255.999 * self.vec[2])}"