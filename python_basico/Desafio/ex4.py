from minhaMath import calculaFatorial
import math

epsilon = 10**(-10)
cont = 0
seno = 0
angulo = int(input("Insira o ângulo para o qual deseja calcular o seno: "))

angulo = math.radians(angulo%360)

while True:
    fatorial = calculaFatorial(2*cont+1)
    termo = (((-1)**cont)*(angulo**(2*cont+1)))/fatorial
    seno+=termo
    if abs(termo)<epsilon: break
    cont+=1
    
print(f"Seno calculado por este código: {seno}")
print(f"Seno calculado pela lib math: {math.sin(angulo)}")
