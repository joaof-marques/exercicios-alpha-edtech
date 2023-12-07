import math

x = int(input("Insira um valor inteiro para calcular a raiz quadrada: "))

epsilon = 10**(-6)
def calculaRaizQuadrada(r):
    
    proxR = (r +(x/r))/2
    diff = proxR - r
    if abs(diff) <= epsilon:
        return proxR
    return calculaRaizQuadrada(proxR)

raiz = calculaRaizQuadrada(x)
print(f"A raiz quadrada calculada por este código é {raiz}")
print(f"A raiz quadrada calculada pela biblioteca math é {math.sqrt(x)} ")
print(f"A raiz quadrada calculada usando como expoente o inverso de 2 é {x**(1/2)}")