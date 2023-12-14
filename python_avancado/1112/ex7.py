lista_generator = ((num for num in range(1, 11) if num%2==0) if coluna%2==0 else (num for num in range(1, 11) if num%2==1) for coluna in range(1, 5))

for linha in lista_generator:
    for coluna in linha:
        print(coluna, end =" ")
    print()


print("----------------------------------------------------------------------")

linha_impar = (num for num in range(1, 11) if num%2==1)
linha_par = (num for num in range(1, 11) if num%2==0)


lista_generator = (linha_par if coluna%2==0 else linha_impar for coluna in range(1, 5))

for pos, linha in enumerate(lista_generator):
    print(f"linha {pos+1}: ", end="")
    for coluna in linha:
        print(coluna, end =" ")
    print()