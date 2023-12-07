maior = 0
soma = 0

for i in range(1,6):
    num = float(input(f"Insira o {i}° número: "))
    if num > maior:
        maior = num
    soma += num

media = soma/5

print(f"O maior numero informado foi {maior}")
print(f"A soma dos números informados é {soma}")
print(f"A média dos números informados é {media}")