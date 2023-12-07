frase = input("Insira uma frase: ")
fraseFinal = ""
testeVogal = False

for letra in frase:
    for vogal in "aeiou":
        if letra.lower() == vogal:
            testeVogal = True
            continue
    
    if testeVogal:
        fraseFinal += ""
        testeVogal = False
    else: fraseFinal += letra
    
        
print(fraseFinal)