import math

print("Olá! Vamos encontrar o maior número entre 3 inteiros?")
a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

maiorAB = (a+b)/2 + abs(a-b)/2
maiorABC = (maiorAB+c)/2 + abs(maiorAB-c)/2

print(f"O maior valor é: {maiorABC:.0f}")