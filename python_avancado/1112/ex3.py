class iteradorListas ():
    def __init__(self, lista):
        self.lista = lista
        self.indice = 0
        
    def __iter__ (self):
        return self
    
    def __next__(self):
        
        if self.indice <= len(self.lista)-1:
            result = self.lista[self.indice]
            self.indice+=1
            return result
        else: raise StopIteration


lista = [1, 2, 3, 4, 5]
iterador = iteradorListas(lista)

while True:
    try:
        print(next(iterador))
    except StopIteration:
        print("Fim da iteração")
        break