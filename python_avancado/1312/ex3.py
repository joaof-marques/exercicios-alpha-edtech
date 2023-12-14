estoque = [("abacate", 10, 2), ("abacaxi", 30,1), ("maçã", 8,2.5), ("banana", 12, 4)]

#Utilizei o sorted pois não queria alterar a lista original. Se eu tivesse utilizado o método sort() a lista original teria sido alterada
# o argumento key serve para definir um parâmetro de ordenação, como eu queria ordenar pela quantidade, informei o x[1]
estoque_ordenado = sorted(estoque, key= lambda x: x[1]*x[2])

print(estoque)
print(estoque_ordenado)