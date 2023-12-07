numeros = []
while True:
    x = int(input("Insira um número: "))
    if x == 0:
        break
    numeros.append(x)


def multiplicaValores(*args):
    total = 1
    for num in args:
        total *= num
        
    return total

multiplicados = multiplicaValores(*numeros)
print(f"O resultado da multiplicação é {multiplicados}")