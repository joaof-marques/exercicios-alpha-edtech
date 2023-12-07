#Angulo A
angulo = float(input("Digite o ângulo A: "))

#Quantidade de estadios entre as duas cidades (referentes ao Angulo A)
qtdeEstadios = float(input("Digite a quantidade de estádios entre as duas Cidades: "))

#divide a qtdeEstadios pelo angulo para descobrir a razão de estadio para 1°
#multiplica por 360 para descobrir a distancia do planeta
circunferenciaEstadios = (360*qtdeEstadios)/angulo

#converte para km utilizando o valor informado no problema
circunferenciaKm = (circunferenciaEstadios * 176.4)/1000

print(f"A circunferência do planeta em estadios é: {circunferenciaEstadios}")
print(f"A circunferência do planeta em KMs é: {circunferenciaKm}")