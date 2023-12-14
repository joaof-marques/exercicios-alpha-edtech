inteiros = [1, 2, 3, 4, 5, 6 ,7, 8, 9, 10]

def aplica_funcoes_secundarias(inteiros, funcao1, funcao2):
    resultado1 = funcao1(inteiros)
    resultado2 = funcao2(resultado1)
    return resultado2

def triplica_valores(numeros):
    numeros_triplicados = []
    for i in numeros:
        numeros_triplicados.append(i*3)
    return numeros_triplicados

def filtra_impares(numeros):
    numeros_impares= []
    for i in numeros:
        if i%2==1:
            numeros_impares.append(i)
    return numeros_impares

resultado_final = aplica_funcoes_secundarias(inteiros, triplica_valores, filtra_impares)
print(resultado_final)