numeroBase = int(input("Insira um número para gerar a tabuada: "))

for i in range(1, 11):
    print(f"{numeroBase} x {i} = {numeroBase*i}")