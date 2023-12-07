import math

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
x = float(input("Digite o primeiro número em ponto flutuante: "))
y = float(input("Digite o segundo número em ponto flutuante: "))

expressao = a + b*x - math.sqrt(b) + ((a+b)/(x-y))

print(f"O resultado da expressão para os valores informados é: {expressao:.2f}")