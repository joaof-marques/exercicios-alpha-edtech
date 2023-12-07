frase = input("Insira uma frase: ")
pantograma = True
alfabeto = "abcdefghijklmnopqrstuvwxyz"
testeLetra = False

for letra in alfabeto:
    for caractere in frase:
        if caractere.lower() == letra.lower():
            testeLetra = True
            continue
    
    if not testeLetra:
        pantograma = False
        break
    testeLetra = False
        


if pantograma:
    print("A frase informada é um pantograma!")
else: print("A frase informada não é um pantograma")


#Exemplo de frase para obter true: "The quick brown fox jumps over the lazy dog"