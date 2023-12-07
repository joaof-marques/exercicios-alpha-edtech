# -*- coding: <encoding name> -*-

def validaSenha (senha):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    numeros = '1234567890'
    caracteresEspeciais = "!@#$%*()_+=-/*?,.<>[]{}`'~^;:"
    print("\n")

    tamanhoMinimo = "\u2713"  if len(senha) > 8  else  "X"
    letraMinuscula = "\u2713" if any(letra in alfabeto for letra in senha)  else  "X"
    letraMaiuscula = "\u2713" if any(letra in alfabeto.upper() for letra in senha)  else  "X"
    contemNumero = "\u2713" if any(caractere in numeros for caractere in senha)  else  "X"
    contemCaractereEspecial = "\u2713" if any(caractere in caracteresEspeciais for caractere in senha)  else  "X"

    print("Quandidade mínima de caracteres: ", tamanhoMinimo)
    print("Presença de letra minúscula: ", letraMinuscula)
    print("Presença de letra maiúscula: ", letraMaiuscula)
    print("Presença de números: ", contemNumero)
    print("Presença de caracteres especiais: ", contemCaractereEspecial)

    if "X" in [tamanhoMinimo, letraMaiuscula, letraMinuscula, contemNumero, contemCaractereEspecial]:
        print("\nSenha Reprovada. Tente uma nova")
    else: print("\nSenha aprovada.")
    
    
validaSenha("123456789Ab!")
validaSenha("1a2B3c4D=+")
validaSenha("1234Ab!")
validaSenha("1234ab!")
validaSenha("1234ab")
validaSenha("1234b")