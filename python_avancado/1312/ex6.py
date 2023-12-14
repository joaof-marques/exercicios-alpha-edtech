from functools import reduce

pessoas = [{"pessoa1": "João"}, {"pessoa2": "Paulo"}, {"pessoa3": "Mauricio"}]


#além de utilizar reduce e lambda, utilizei o ** (unpacking)
dicionario_unico = reduce(lambda acumulador, x: {**acumulador, **x}, pessoas)

print(dicionario_unico)