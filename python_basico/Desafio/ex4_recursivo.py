from minhaMath import calculaFatorial
import math

epsilon = 10**(-10)
angulo = int(input("Insira o ângulo para o qual deseja calcular o seno: "))
angulo = math.radians(angulo%360)
seno = angulo #Essa inicialização representa o primeiro termo (x/1!)

def senoRecursivo (numerador, denominador, incrementoFatorial, k):
    novoNumerador = numerador * angulo * angulo
    novoDenominador = denominador * (incrementoFatorial + 1) * (incrementoFatorial + 2)
    termo = ((-1)**k)*(novoNumerador/novoDenominador)
    if abs(termo) <= epsilon:
        return 0
    else: return termo + senoRecursivo(novoNumerador, novoDenominador, incrementoFatorial+2, k+1)

    
seno += senoRecursivo(angulo, 1, 1, 1)
print(f"Seno calculado por este código: {seno}")
print(f"Seno calculado pela lib math: {math.sin(angulo)}")

#Não consegui identificar o motivo deste código ter menos precisão do que o outro. Acredito que seja por questões de arredondamento quando passo o numerador e o denominador para outra execução