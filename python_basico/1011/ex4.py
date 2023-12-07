base = int(input("Insira o valor para a base da exponenciação: "))
expoente = int(input("Insira o valor do expoente: "))

resultado = base
if expoente==0:
    print(f"O resultado de {base} elevado a {expoente} é 1")
    exit()
    
for i in range (1, expoente):
    resultado *= base
    
print(f"O resultado de {base} elevado a {expoente} é {resultado}")