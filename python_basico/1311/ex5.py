medicoes = int(input("Insira a quantidade de medições: "))
cont = 1
marcadorQueda = 0
ultimaMed = 11000

while cont <= medicoes:
    medAtual = int(input(f"Insira o valor da medição {cont}: "))
    if medAtual < ultimaMed and marcadorQueda <= 1:
        marcadorQueda = cont
    cont += 1
    ultimaMed = medAtual

#isso é necessário pois a variável ultimaMed foi inicializada com valor alto para a lógica do loop funcionar, então na 1 iteração ele acrescenta um marcador que deve ser desconsiderado
if marcadorQueda == 1:
    print(marcadorQueda-1)
else: print(marcadorQueda)
