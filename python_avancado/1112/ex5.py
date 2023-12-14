def gerar_iterador():
    cont = 0    
    while cont < 10:
        aux = cont
        cont += 1
        yield aux
    else:
        raise StopIteration

    

iterador = gerar_iterador()

while True:
    try:
        print(next(iterador))
    except StopIteration:
        print("Fim do generator")
        break