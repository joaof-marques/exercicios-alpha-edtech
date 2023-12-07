valor = float(input("Insira um número para verificarmos se é inteiro ou decimal: ").replace(",", "."))

if valor%1==0:
    print(f"O número {valor:.0f} é inteiro!")
else:
    print(f"O número {valor} é decimal!")