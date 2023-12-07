valorInteiro = int(input("Digite um valor inteiro para podermos separar as suas cédulas: "))

notasDuzentos = valorInteiro//200
saldo = valorInteiro%200
notasCem = saldo//100
saldo %= 100

notasCinquenta = saldo//50
saldo %= 50

notasVinte = saldo//20
saldo %= 20

notasDez = saldo//10
saldo %= 10

notasCinco = saldo//5
saldo %= 5

notasDois = saldo//2
saldo %= 2

# não é necessário fazer essa atribuição. Podemos usar o saldo direto na soma 
#Fiz apenas para terminar a lógica e facilitar o entendimento
notasUm = saldo

totalCedulas = notasDuzentos + notasCem + notasCinquenta + notasVinte + notasDez + notasCinco + notasDois + notasUm

print(f"O menor número de cédulas para o valor R${valorInteiro} é {totalCedulas}")