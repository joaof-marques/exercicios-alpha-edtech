from typing import List

class InvalidSizesOfLists(Exception):
    def __init__(self, mensagem="As listas não tem o mesmo tamanho"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
        
def opera_listas (lista1:List[int], lista2:List[int]) -> None:
    lista_resultado = []
    
    if len(lista1) != len(lista2):
        raise InvalidSizesOfLists
    
    for i in range(len(lista1)):
        lista_resultado.append(lista1[i]/lista2[i])
        
    print(lista_resultado)
    
    
lista1:List[int] = [4, 6, 8, 10, 12]
lista2:List[int] = [2, 3, 4, 5, 6]
try:
    opera_listas(lista1, lista2)
    
except InvalidSizesOfLists as erro:
    print(erro.mensagem)
except TypeError:
    print("Existem elementos inválidos nas listas. Favor verificar.")
except ZeroDivisionError:
    print("Ocorreu uma divisão por zero. Favor verificar a lista2")