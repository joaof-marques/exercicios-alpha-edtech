def soma_argumentos_nomeados(**kwargs):
    soma=0
    for num in kwargs.values():
        soma+=num
    return soma

resultado = soma_argumentos_nomeados(a=10, b=20, c=1500)

print(resultado)