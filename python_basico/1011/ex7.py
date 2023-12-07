num = int(input("Insira um valor para testar se é ou não primo: "))
ePrimo = True
for i in range (2, num):
    if num%i==0:
        ePrimo = False
        break

if ePrimo:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo!")
    