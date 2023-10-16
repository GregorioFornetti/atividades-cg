
from typing import Union
import numpy as np
from Atividade02.interactive.Vec import Vec


class Vec4(Vec):
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

    def __init__(self, x: np.float64 = 0.0, y: np.float64 = 0.0, z: np.float64 = 0.0, w: np.float64 = 0.0):
        '''
        Construtor da classe Vec4. Recebe as coordenadas x, y, z e w do vetor.

        --- 

        Parâmetros:

            - x: np.float64 = 0.0 - Coordenada x do vetor.

            - y: np.float64 = 0.0 - Coordenada y do vetor.

            - z: np.float64 = 0.0 - Coordenada z do vetor.

            - w: np.float64 = 0.0 - Coordenada w do vetor.
        '''
        if not isinstance(x, np.float64) and not isinstance(x, float) and not isinstance(x, int):
            raise TypeError(f"x precisa ser um número. Tipo recebido: {type(x)}")
        if not isinstance(y, np.float64) and not isinstance(y, float) and not isinstance(y, int):
            raise TypeError(f"y precisa ser um número. Tipo recebido: {type(y)}")
        if not isinstance(z, np.float64) and not isinstance(z, float) and not isinstance(z, int):
            raise TypeError(f"z precisa ser um número. Tipo recebido: {type(z)}")
        if not isinstance(w, np.float64) and not isinstance(w, float) and not isinstance(w, int):
            raise TypeError(f"w precisa ser um número. Tipo recebido: {type(w)}")
        
        self.vec = np.array([x, y, z, w], dtype=np.float64)
    
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
    
    @property
    def w(self) -> np.float64:
        '''
        Coordenada w do vetor.
        '''
        return self.vec[3]

    @w.setter
    def w(self, value: np.float64):
        self.vec[3] = value
    

    def __neg__(self) -> 'Vec4':
        '''
        Inverte o sinal de todas as coordenadas do vetor.

        Exemplo:

        >>> v = Vec4(1, 2, 3, 4)
        >>> print(-v)
        -1.0 -2.0 -3.0 -4.0

        ---

        Retorno:

            - Vec4 - Versão negativa do vetor.
        '''
        return Vec4(-self.vec[0], -self.vec[1], -self.vec[2], -self.vec[3])
    
    def __getitem__(self, key: int) -> np.float64:
        '''
        Retorna a coordenada do vetor de acordo com o índice.

        Exemplo:

        >>> v = Vec4(1, 2, 3, 4)
        >>> print(v[0])
        1.0

        ---

        Parâmetros:
            
            - key: int - Índice da coordenada do vetor (0 = x, y = 1, z = 2 e w = 4).

        ---

        Retorno:
            
            - np.float64 - Valor da coordenada escolhida.
        '''
        return self.vec[key]
    

    def __add__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> print(v1 + v2)
        6.0 8.0 10.0 12.0

        Somando um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> print(v1 + 1)
        2.0 3.0 4.0 5.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec4 - Resultado da soma.

        '''
        if isinstance(other, Vec4):
            return Vec4(self.vec[0] + other.vec[0], self.vec[1] + other.vec[1], self.vec[2] + other.vec[2], self.vec[3] + other.vec[3])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec4(self.vec[0] + other, self.vec[1] + other, self.vec[2] + other, self.vec[3] + other)
        else:
            raise TypeError(f"Tipo inválido para soma, esperado: Vec, np.float64, recebido: {type(other)}")
    
    def __sub__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> print(v1 - v2)
        -4.0 -4.0 -4.0 -4.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> print(v1 - 1)
        0.0 1.0 2.0 3.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser subtraído.

        ---

        Retorno:
            
                - Vec4 - Resultado da subtração.
        
        '''
        if isinstance(other, Vec4):
            return Vec4(self.vec[0] - other.vec[0], self.vec[1] - other.vec[1], self.vec[2] - other.vec[2], self.vec[3] - other.vec[3])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec4(self.vec[0] - other, self.vec[1] - other, self.vec[2] - other, self.vec[3] - other)
        else:
            raise TypeError(f"Tipo inválido para subtração, esperado: Vec, np.float64, recebido: {type(other)}")
    
    def __mul__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> print(v1 * v2)
        5.0 12.0 21.0 32.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> print(v1 * 2)
        2.0 4.0 6.0 8.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec4 - Resultado da multiplicação.
        '''
        if isinstance(other, Vec4):
            return Vec4(self.vec[0] * other.vec[0], self.vec[1] * other.vec[1], self.vec[2] * other.vec[2], self.vec[3] * other.vec[3])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec4(self.vec[0] * other, self.vec[1] * other, self.vec[2] * other, self.vec[3] * other)
        else:
            raise TypeError(f"Tipo inválido para multiplicação, esperado: Vec, np.float64, recebido: {type(other)}")
    
    def __truediv__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> print(v1 / v2)
        0.2 0.33 0.43 0.5

        Dividindo um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> print(v1 / 2)
        0.5 1.0 1.5 2.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser utilizado como divisor.

        ---

        Retorno:

            - Vec4 - Resultado da divisão.
        '''
        if isinstance(other, Vec4):
            return Vec4(self.vec[0] / other.vec[0], self.vec[1] / other.vec[1], self.vec[2] / other.vec[2], self.vec[3] / other.vec[3])
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            return Vec4(self.vec[0] / other, self.vec[1] / other, self.vec[2] / other, self.vec[3] / other)
        else:
            raise TypeError(f"Tipo inválido para divisão, esperado: Vec, np.float64, recebido: {type(other)}")


    def __iadd__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Soma elemento a elemento de dois vetores. Ou soma um número a cada elemento do vetor.

        Exemplo:

        Somando dois vetores:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> v1 += v2
        >>> print(v1)
        6.0 8.0 10.0 12.0

        Somando um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v1 += 1
        >>> print(v1)
        2.0 3.0 4.0 5.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser somado.
        
        ---

        Retorno:

            - Vec4 - Resultado da soma.
        '''
        if isinstance(other, Vec4):
            self.vec[0] += other.vec[0]
            self.vec[1] += other.vec[1]
            self.vec[2] += other.vec[2]
            self.vec[3] += other.vec[3]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] += other
            self.vec[1] += other
            self.vec[2] += other
            self.vec[3] += other
        else:
            raise TypeError(f"Tipo inválido para soma, esperado: Vec, np.float64, recebido: {type(other)}")
        return self
    
    def __isub__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Subtrai elemento a elemento de dois vetores. Ou subtrai um número a cada elemento do vetor.

        Exemplo:

        Subtraindo dois vetores:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> v1 -= v2
        >>> print(v1)
        -4.0 -4.0 -4.0 -4.0

        Subtraindo um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v1 -= 1
        >>> print(v1)
        0.0 1.0 2.0 3.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser subtraído.
        
        ---

        Retorno:

            - Vec4 - Resultado da subtração.
        '''
        if isinstance(other, Vec4):
            self.vec[0] -= other.vec[0]
            self.vec[1] -= other.vec[1]
            self.vec[2] -= other.vec[2]
            self.vec[3] -= other.vec[3]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] -= other
            self.vec[1] -= other
            self.vec[2] -= other
            self.vec[3] -= other
        else:
            raise TypeError(f"Tipo inválido para subtração, esperado: Vec, np.float64, recebido: {type(other)}")
        return self
    
    def __imul__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Multiplica elemento a elemento de dois vetores. Ou multiplica um número a cada elemento do vetor.

        Exemplo:

        Multiplicando dois vetores:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> v1 *= v2
        >>> print(v1)
        5.0 12.0 21.0 32.0

        Multiplicando um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v1 *= 2
        >>> print(v1)
        2.0 4.0 6.0 8.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser multiplicado.
        
        ---

        Retorno:

            - Vec4 - Resultado da multiplicação.
        '''
        if isinstance(other, Vec4):
            self.vec[0] *= other.vec[0]
            self.vec[1] *= other.vec[1]
            self.vec[2] *= other.vec[2]
            self.vec[3] *= other.vec[3]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] *= other
            self.vec[1] *= other
            self.vec[2] *= other
            self.vec[3] *= other
        else:
            raise TypeError(f"Tipo inválido para multiplicação, esperado: Vec, np.float64, recebido: {type(other)}")
        return self

    def __itruediv__(self, other: Union['Vec4', np.float64]) -> 'Vec4':
        '''
        Divide elemento a elemento de dois vetores. Ou divide um número a cada elemento do vetor.

        Exemplo:

        Dividindo dois vetores:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> v1 /= v2
        >>> print(v1)
        0.2 0.33 0.43 0.5

        Dividindo um vetor e um número:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v1 /= 2
        >>> print(v1)
        0.5 1.0 1.5 2.0

        ---

        Parâmetros:

            - other: Union['Vec4', np.float64] - Vetor ou número a ser dividido.
        
        ---

        Retorno:

            - Vec4 - Resultado da divisão.
        '''
        if isinstance(other, Vec4):
            self.vec[0] /= other.vec[0]
            self.vec[1] /= other.vec[1]
            self.vec[2] /= other.vec[2]
            self.vec[3] /= other.vec[3]
        elif isinstance(other, np.float64) or isinstance(other, float) or isinstance(other, int):
            self.vec[0] /= other
            self.vec[1] /= other
            self.vec[2] /= other
            self.vec[3] /= other
        else:
            raise TypeError(f"Tipo inválido para divisão, esperado: Vec, np.float64, recebido: {type(other)}")
        return self
    
    def __repr__(self) -> str:
        '''
        Retorna uma string representando o vetor.

        A string é composta pelas coordenadas x, y e z do vetor, separadas por um espaço.

        Exemplo:

        >>> v = Vec4(1, 2, 3, 4)
        >>> print(v)
        1.0 2.0 3.0 4.0
        '''
        return f"{self.vec[0]} {self.vec[1]} {self.vec[2]} {self.vec[3]}"
    
    
    def length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor.

        Exemplo:

        >>> v = Vec4(1, 2, 3, 4)
        >>> print(v.length())  # sqrt(1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2)
        5.477225575051661
        '''
        return np.sqrt(self.squared_length())
    
    def squared_length(self) -> np.float64:
        '''
        Retorna o comprimento do vetor ao quadrado.

        Exemplo:

        >>> v = Vec4(1, 2, 3, 4)
        >>> print(v.squared_length())  # 1 ** 2 + 2 ** 2 + 3 ** 2 + 4 ** 2
        30.0
        '''
        return self.vec[0] ** 2 + self.vec[1] ** 2 + self.vec[2] ** 2 + self.vec[3] ** 2
    
    def dot(self, other: 'Vec4') -> np.float64:
        '''
        Retorna o produto escalar entre dois vetores.

        Exemplo:

        >>> v1 = Vec4(1, 2, 3, 4)
        >>> v2 = Vec4(5, 6, 7, 8)
        >>> print(v1.dot(v2))
        70.0

        ---

        Parâmetros:

            - other: 'Vec4' - Segundo vetor do produto escalar.
        
        ---

        Retorno:
            
            - np.float64 - Resultado do produto escalar.
        '''
        if not isinstance(other, Vec4):
            raise TypeError(f"Tipo inválido para produto escalar, esperado: Vec4, recebido: {type(other)}")
        
        return self.vec[0] * other.vec[0] + self.vec[1] * other.vec[1] + self.vec[2] * other.vec[2] + self.vec[3] * other.vec[3]
    
    def unit_vector(self) -> 'Vec4':
        '''
        Retorna o vetor unitário.

        Exemplo:

        >>> v = Vec4(1, 2, 3, 4)
        >>> print(v.unit_vector())
        0.18 0.37 0.58 0.73

        ---

        Retorno:

            - Vec4 - Vetor unitário.
        '''
        return self / self.length()

Point4 = Vec4