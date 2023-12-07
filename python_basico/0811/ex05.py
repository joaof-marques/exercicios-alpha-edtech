def trocaVogais (frase):
    frase = frase.replace("a", "*")
    frase = frase.replace("e", "*")
    frase = frase.replace("i", "*")
    frase = frase.replace("o", "*")
    frase = frase.replace("u", "*")
    return frase
    

teste = trocaVogais("abacate")
print(teste)