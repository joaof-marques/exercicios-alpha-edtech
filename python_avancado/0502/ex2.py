lista = [3,6,7,9,15,18,24,32,40]

def busca_binaria_recursiva(lista, termo, cont=0):
    
    if len(lista) <= 1 and lista[0] != termo:
        return "Elemento não encontrado"
    
    meio = len(lista)//2
    
    if termo == lista[meio]:
        return f"O elemento está na posição {meio+cont}"
    elif termo < lista[meio]:
        return busca_binaria_recursiva(lista[:meio], termo, cont)
    else:
        return busca_binaria_recursiva(lista[meio:], termo, cont+meio)
    

print(busca_binaria_recursiva(lista, 40))