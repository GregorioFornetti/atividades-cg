'''
    Funções utilitárias que podem ser necessárias em qualquer parte do código.
'''
import random

from Atividade04.src.constants import pi

def degrees_to_radians(degrees: float):
    '''
    Converte um ângulo de graus para radianos.

    ---

    Parâmetros:

        - degrees: float - Ângulo em graus.
    
    ---

    Retorno:

        - float - Ângulo em radianos.
    '''
    return degrees * pi / 180.0

def random_double():
    '''
    Gera um número aleatório entre 0 e 1.

    ---

    Retorno:

        - float - Número aleatório entre 0 e 1.
    '''
    return random.random()