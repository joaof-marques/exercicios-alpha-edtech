qtdeInt = int(input("Insira a quantidade de números: "))

cont = 0
soma = 0

while cont < qtdeInt:
    soma += float(input(f"Insira o {cont+1}° número: "))
    cont+=1
    
print(f"A soma de todos os números informados é: {soma:.2f}")