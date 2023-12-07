equacao = input("Insira a equação: ")
parentesisAberto = 0
parentesisFechado = 0

for caractere in equacao:
    if caractere == "(":
        parentesisAberto+=1
    elif caractere == ")":
        parentesisFechado += 1
        
if parentesisAberto == parentesisFechado:
    print("Correto")
else: print("Incorreto")