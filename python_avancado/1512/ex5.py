from typing import List

lista:List[int] = [1, 2, 3, 4, 5]

class ArquivoVazio(Exception):
    def __init__(self, mensagem="O arquivo está vazio"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

def testa_limites_lista(lista: List[int], indice:int)->int:
    if indice <= len(lista)-1:
        return lista[indice]
    
    le_arquivo('txtTeste.txt')
    raise IndexError
    

def le_arquivo(nome_arquivo:str) -> None:    
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        
        if len(conteudo)==0:
            raise ArquivoVazio
        
        print(conteudo)

try:
    print(testa_limites_lista(lista, 5))
except IndexError as error:
    print("O índice está fora da lista")
except FileNotFoundError as erro:
    print("Arquivo não encontrado, tente novamente com outro nome")
except PermissionError as erro:
    print("Você não tem permissão para acessar/modificar o arquivo.")
except ArquivoVazio as erro:
    print(erro.mensagem)