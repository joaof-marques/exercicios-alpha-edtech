# import fatorial
# import outroFatorial

# print(fatorialTeste)  #Essa linha vai dar um erro pois fatorialTeste não está definido neste módulo

# print(fatorial.fatorialTeste) #2432902008176640000
# print(outroFatorial.fatorialTeste) #720

#Note a diferença entre os valores. Por mais que tenham os mesmos nomes, o nameSpace garante que você diga de qual pacote ele deve puxar a variável fatorialTeste

#Caso você importe utilizando aliases 
from fatorial import fatorialTeste as resultadoFatorial
from outroFatorial import fatorialTeste as resultadoFatorial

#se realizarmos o print de resultadoFatorial vamos obter:
print(resultadoFatorial) #720
#Isso ocorre pois no primeiro import ele aloca em resultadoFatorial o valor que vem do módulo fatorial
#Na segunda linha ele sobrescreve o valor de resultadoFatorial com o valor que vem de outroFatorial.
#É a mesma lógica de:
# num1 = 10
# num1 = 30
#Se printarmos o valor de num1 vamos receber 30, pois o valor foi sobrescrito