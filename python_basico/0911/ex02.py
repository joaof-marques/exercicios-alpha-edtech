nota1 = float(input("Digite a nota parcial 01: ").replace(",", "."))
nota2 = float(input("Digite a nota parcial 02: ").replace(",", "."))
nota3 = float(input("Digite a nota parcial 03: ").replace(",", "."))

media = (nota1+nota2+nota3)/3

if media == 10:
    print(f"Média atingida: {media:.2f} / Situação: Aprovado com Distinção")
elif media >= 7:
    print(f"Média atingida: {media:.2f} / Situação: Aprovado")
else:
    print(f"Média atingida: {media:.2f} / Situação: Reprovado")