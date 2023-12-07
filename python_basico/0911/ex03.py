valorSaque = float(input("Insira o valor a ser sacado: ").replace(",", "."))

if valorSaque<10 or valorSaque > 1000:
    print("O valor informado é inválido. Favor informar um valor entre 10 e 1000")
    exit()
if(valorSaque%1!=0):
    print("Favor informar um valor inteiro. Esta máquina não disponibiliza saque em moedas")
    exit()

saldo = valorSaque
notasDois = 0

if valorSaque%10==1:
    notasDois = 1
    saldo = valorSaque-2
elif valorSaque%10==3:
    notasDois = 2
    saldo = valorSaque-4
    

notasDuzentos = saldo//200
saldo %= 200

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

notasDois += saldo//2

totalCedulas = notasDuzentos + notasCem + notasCinquenta + notasVinte + notasDez + notasCinco + notasDois

print(f"Serão liberadas:\n {notasDuzentos:.0f} notas de R$ 200,\n {notasCem:.0f} notas de R$ 100,\n {notasCinquenta:.0f} notas de R$ 50,\n {notasVinte:.0f} notas de R$ 20,\n {notasDez:.0f} notas de R$ 10,\n {notasCinco:.0f} notas de R$ 5,\n {notasDois:.0f} notas de R$ 2,\n totalizando R$ {valorSaque:.0f}")