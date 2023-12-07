frase = input("Insira uma frase: ").lower()
caractereCentral = int(round(len(frase)/2, 0))
fraseFiltrada = "" #apenas letras
ehLetra = False
cont = 0
palindromo = True

for caractere in frase:
    for letra in "abcdefghijklmnopqrstuvwxyz":
        if caractere == letra:
            ehLetra = True
            break
    
    if ehLetra:
        fraseFiltrada += caractere
        ehLetra = False
            

while cont != caractereCentral:
    
    if fraseFiltrada[cont] != fraseFiltrada[len(fraseFiltrada)-1-cont]:
        palindromo = False
        break    
    
    cont += 1
    
if palindromo:
    print("É palíndromo!")
else: print("Não é palíndromo =/")