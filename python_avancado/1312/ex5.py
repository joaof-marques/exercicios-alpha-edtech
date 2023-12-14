lista_de_listas = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]

lista_simples = []

list(map(lambda x: lista_simples.extend(x), lista_de_listas))

print(lista_de_listas)
print(lista_simples)