lista_pares = [num for num in range(1, 11) if num%2==0]
generator_pares = (num for num in range(1, 11) if num%2==0)


print(lista_pares)

while True:
    print(next(generator_pares))
    