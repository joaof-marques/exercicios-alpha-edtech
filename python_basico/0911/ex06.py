print("Insira dois números e em seguida informe a operação matemática desejada.")
print("Operações disponíveis: + (soma), - (subtração), x (multiplicação) e / (divisão)")
num1 = float(input("Insira o número 1: ").replace(",", "."))
num2 = float(input("Insira o número 2: ").replace(",", "."))
operacao = input("Insira a operação desejada: ")
resultado = 0

if operacao == "+":
    resultado = num1+num2
elif operacao == "-":
    resultado = num1-num2
elif operacao == "x":
    resultado = num1*num2
elif operacao == "/":
    resultado = num1/num2
else: 
    print("Operação Inválida!")
    exit()
    
if resultado%1!=0:
    print(f"O resultado {resultado} é um número decimal, portanto, não pode ser classificado como par e nem como ímpar")
elif resultado%2==0:
    print(f"O resultado {resultado} é par!")
else: print(f"O resultado {resultado} é ímpar!")

if resultado >= 0:
    print(f"O resultado {resultado} é positivo!")
else: print(f"O resultado {resultado} é negativo!")

if resultado%1==0:
    print(f"O resultado {resultado} é inteiro!")
else:
    print(f"O resultado {resultado} é decimal!")