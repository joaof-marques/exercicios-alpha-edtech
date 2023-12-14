class Fibonacci:
    
    # função onde iniciamos a classe e os valores base são setados
    # maximo define o valor máximo dos elementos da sequência e não a quantidade de elementos
    def __init__(self, maximo = 1000000):
        self.elemento_atual = 0
        self.proximo_elemento = 1
        self.maximo = maximo
    
    # o __iter__ retorna o próprio elemento self, pois já estamos implementando o método __next__ na classe, fazendo com que ela seja um iterador e também um iterável
    def __iter__(self):
        return self
    
    # Método responsável por fazer o "andamento" dos cálculos fibonacci
    # Segue o mesmo raciocínio de um loop for convencional, usando um 3 elemento como auxiliar para a troca e soma dos valores
    def __next__(self):
        if self.proximo_elemento > self.maximo:
            raise StopIteration
        
        valor_auxiliar = self.elemento_atual
        self.elemento_atual = self.proximo_elemento
        self.proximo_elemento += valor_auxiliar
        
        return valor_auxiliar
    
fib1 = Fibonacci()

# Utilizando a característica de objeto iterável, podemos usar um for para percorrer os dados
print("Utilizando o For")
try:
    for i in fib1:
        print(i)
except StopIteration:
    print("Estouro o valor máximo")


# Utilizando a característica de um objeto iterador, podemos utilizar o next() junto com o Stopiteration para percorrer os dados
fib2 = Fibonacci()
print("Utilizando o next")
while True:
    try:
        elemento = next(fib2)
        print(elemento)
    except StopIteration:
        break