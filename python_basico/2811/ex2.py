#Caso quisesse, poderia ter recebido os argumentos em um *args e acessado através da posição na tupla
def multiplicar_lista(lista, valor):

    #Utiliza list comprehension para sintetizar a sintaxe do for. Ponto positivo
    return [elemento * valor for elemento in lista]

 

numeros = [1, 2, 3, 4, 5]

#Atribui a lista retornada à uma variável. Não seja a ser um ponto negativo, porém, se o objetivo for apenas printar, pode ser passado direto no print
novo_numeros = multiplicar_lista(numeros, 3)

print(novo_numeros)