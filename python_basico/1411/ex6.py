frase = input("Insira uma frase: ")

for caractere in frase:
    if caractere == caractere.lower():
        print(caractere.upper(), end="")
    else:
        print(caractere.lower(), end="")
        
#Esse print serve apenas para não imprimir a interrupção de impressão (%)
print()
        