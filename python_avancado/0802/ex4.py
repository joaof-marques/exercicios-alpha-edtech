import pprint, time
from lista_filmes import filmes_recomendados



class Filme:
    def __init__(self, dict_filme) -> None:
        self.titulo = dict_filme['titulo']
        self.ano = dict_filme['ano']
        self.relevancia = dict_filme['relevancia']
        
    def __str__(self) -> str:
        return f"Titulo: {self.titulo}\t|\tAno: {self.ano}\t|\tRelevância: {self.relevancia}"

class Sistema_recomendacao_filmes:
    def __init__(self) -> None:
        self.lista_filmes_merge = []
        self.lista_filmes_quick = []
        self.tempo_merge = 0
        self.tempo_quick = 0
        
    def inserir_filme_catalogo(self, filme: Filme) -> None:
        self.lista_filmes_merge.append(filme)
        self.lista_filmes_quick.append(filme)
        
    def merge_sort(self, catalogo): #Ordena os filmes do catálogo utilizando merge sort
        if len(catalogo) > 1:
            meio = len(catalogo)//2
            esquerda = catalogo[:meio]
            direita = catalogo[meio:]
            
            self.merge_sort(esquerda)
            self.merge_sort(direita)
            
            contEsq = contDir = contGeral = 0
            while contEsq < len(esquerda) and contDir < len(direita):
                if esquerda[contEsq].relevancia > direita[contDir].relevancia:
                    catalogo[contGeral] = esquerda[contEsq]
                    contEsq += 1
                elif esquerda[contEsq].relevancia < direita[contDir].relevancia:
                    catalogo[contGeral] = direita[contDir]
                    contDir += 1
                else:
                    if int(esquerda[contEsq].ano) < int(direita[contDir].ano):
                        catalogo[contGeral] = direita[contDir]
                        contDir += 1
                    else: 
                        catalogo[contGeral] = esquerda[contEsq]
                        contEsq += 1
                contGeral += 1
                
            while contEsq < len(esquerda):
                catalogo[contGeral] = esquerda[contEsq]
                contEsq += 1
                contGeral += 1
                
            while contDir < len(direita):
                catalogo[contGeral] = direita[contDir]
                contDir += 1
                contGeral += 1
        
        return catalogo
    
    
    def quick_sort(self, catalogo):
        if len(catalogo) <= 1:
            return catalogo
        else:
            pivo = catalogo[-1]
            menores = []
            maiores = []
            
            for filme in catalogo[:-1]:
                if filme.relevancia < pivo.relevancia:
                    menores.append(filme)
                elif filme.relevancia > pivo.relevancia:
                    maiores.append(filme)
                else:
                    if filme.ano > pivo.ano:
                        menores.append(filme)
                    else:
                        maiores.append(filme)
        print(f'{[menor.relevancia for menor in menores]} | {[pivo.relevancia]} | {[maior.relevancia for maior in maiores]}')
        return self.quick_sort(menores)+[pivo]+self.quick_sort(maiores)
        
    def obter_catalogo_recomendado(self):
        inicio = time.time()
        self.merge_sort(self.lista_filmes_merge)
        fim = time.time()
        self.tempo_merge = fim - inicio
        
        inicio = time.time()            
        self.lista_filmes_quick = self.quick_sort(self.lista_filmes_quick.copy())
        fim = time.time()
        self.tempo_quick = fim - inicio
        

    
if __name__ == "__main__":
    netflix = Sistema_recomendacao_filmes()
    
    for filme in filmes_recomendados:
        netflix.inserir_filme_catalogo(Filme(filme))
        
    netflix.obter_catalogo_recomendado()
    
    print("----- MERGE -----")
    for filme in netflix.lista_filmes_merge:
        print(filme)
        
    print("----- QUICK -----")
    for filme in reversed(netflix.lista_filmes_quick):
        print(filme)
    
    print('\n')
    print(f"Tempo execução merge: {netflix.tempo_merge:.40f}")
    print(f"Tempo execução quick: {netflix.tempo_merge:.40f}")