tempo = int(input("Insira o tempo desejado (em segundos): "))

cont = 2

while tempo >= 0:
    print(f"Faltam {tempo} segundos")
    tempo -= cont
    cont+=2
    
print("Acabou")