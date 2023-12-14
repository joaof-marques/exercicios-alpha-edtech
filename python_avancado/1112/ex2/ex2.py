def geraFibonacci(maximo):
    elemento_atual = 0
    proximo_elemento = 1
    
    while proximo_elemento < maximo:
        yield elemento_atual
    
        aux = elemento_atual
        elemento_atual = proximo_elemento
        proximo_elemento += aux
    
gen = geraFibonacci(100000)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))