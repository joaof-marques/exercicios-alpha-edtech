numeros = [1, 2, 3, 4, 5]

def duplicaNumeros (numeros):
    for i in range(0,len(numeros)-1):
        numeros[i] = numeros[i]*2


print(f"lista antes da função: {numeros}")
duplicaNumeros(numeros)
print(f"lista após a função: {numeros}")