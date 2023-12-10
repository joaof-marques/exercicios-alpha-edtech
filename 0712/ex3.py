from typing import Union, Tuple
import random

def gera_resultado_aleatorio () -> Tuple[Union[int, bool, str], Union[int, bool, str]]:
    info: list[Union[int, bool, str]] = [1, 2, 3, 'a', 'b', 'c', True, False]
    return info[random.randint(0,7)], info[random.randint(0,7)]

def verifica_tipos_iguais(a: Union[int, bool, str], b: Union[int, bool, str]):
    if type(a) == type(b):
        print("Sucesso! Os tipos de A e B são iguais!")
    else: print("Tente novamente! Os tipos não foram iguais dessa vez")
    
a, b = gera_resultado_aleatorio()
print(a, b)
verifica_tipos_iguais(a, b)