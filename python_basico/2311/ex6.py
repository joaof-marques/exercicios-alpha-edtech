def contarQtdePalavras (frase):
    qtdePalavras = 0
    for i in range(len(frase)):
        if frase[i] == ' ':
            qtdePalavras+=1
            
    return qtdePalavras+1

print(contarQtdePalavras("Olá, como vai você?"))
print(contarQtdePalavras("Escreva uma função que conte o número de palavras em uma frase inserida pelo usuário. Deve testar a função com alguns valores na programação, não precisa solicitar ao usuário para digitar."))
