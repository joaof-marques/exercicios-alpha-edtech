nomeCompleto = input("Digite o nome completo: ")
ultimoEspaco = nomeCompleto.rfind(" ")
ultimoSobrenome = nomeCompleto[ultimoEspaco+1:]

nomeFormatadoABNT = ultimoSobrenome[0].upper() + ultimoSobrenome[1:].lower() + ", " + nomeCompleto[0] + ". "

cont = 0

while True:
    espaco = nomeCompleto.find(" ", cont+1)
    if espaco == ultimoEspaco:
        break
    nomeFormatadoABNT += nomeCompleto[espaco+1].upper() + ". "
    
    cont = espaco


print(nomeFormatadoABNT)