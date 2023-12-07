frase1 = input("Insira a frase1: ").upper()
frase2 = input("Insira a frase2: ").upper()
letrasComum = ""
letraJaRegistrada = False

for letra1 in frase1:
    for letra2 in frase2:
        if letra1 == letra2:
            for letraComum in letrasComum:
                if letra1 == letraComum:
                    letraJaRegistrada = True
                    break
        
            if not letraJaRegistrada:
                letrasComum += letra1
                break
            letraJaRegistrada = False
            
print(letrasComum)