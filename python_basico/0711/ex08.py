import math

print("Verificador de raízes Bháskara")
a = float(input("Insira o valor do primeiro coeficiente (a): "))
b = float(input("Insira o valor do segundo coeficiente (b): "))
c = float(input("Insira o valor do terceiro coeficiente (c): "))
x = float(input("Insira o valor da raiz desejada: "))

delta = b**2 - (4*a*c)
raiz1 = (-b + math.sqrt(delta)) / (2*a)
raiz2 = (-b - math.sqrt(delta)) / (2*a)


xIgualRaiz1 = raiz1 == x
xIgualRaiz2 = raiz2 == x

print(f"x = raiz1: {xIgualRaiz1}")
print(f"x = raiz2: {xIgualRaiz2}")