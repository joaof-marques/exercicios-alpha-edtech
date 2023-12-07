num = int(input("Insira um valor para calcular o fatorial: "))
resFatorial = 1
qtdeZeros = 0

for i in range (num, 0, -1):
    resFatorial *= i

aux = resFatorial

for i in range (500,):
    if aux%10==0:
        qtdeZeros+=1
        aux=aux//10
    else:
        break

print(f"O fatorial de {num} é {resFatorial}, e tem {qtdeZeros} zero no final do número")