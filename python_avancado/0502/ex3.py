lista = [1, 2, 15, 3, 4, 5, 6, 7, 8, 9, 10, 11, 24]

def somatorio_recursivo(lista):
    if len(lista) > 1:
        return lista[-1]+somatorio_recursivo(lista[:-1])
    return lista[0]

print(somatorio_recursivo(lista))