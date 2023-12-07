caractere = input("Insira um caractere: ")
frase = input("Insira uma string: ")
fraseFinal = ""

for letra in frase:
    if(letra.lower() == caractere.lower()):
        fraseFinal += ""
    else: fraseFinal += letra
        
print(fraseFinal)