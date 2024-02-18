from typing import List

lista:List[int] = [1, 2, 3, 4, 5]

def testa_limites_lista(lista: List[int], indice:int)->int:
    if indice <= len(lista)-1:
        return lista[indice]
    
    raise IndexError

try:
    print(testa_limites_lista(lista, 5))
except IndexError as error:
    print("O índice está fora da lista")