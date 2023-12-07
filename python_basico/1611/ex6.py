import statistics

# numeroAcoes = int(input("Insira o tamanho do array de ações: "))

# acoes = [[],[],[], []] #[[quantidades], [precos], [nomes], valorTotalAções]
# cont = 0

# #alimentar o banco de dados de ações
# while cont < numeroAcoes:
#     qtdeAcao = int(input(f"Insira a quantidade da ação {cont+1}: "))
#     precoAcao = float(input(f"Insira ao preço da ação {cont+1}: ").replace(",", "."))
#     nomeComprador = input("Insira o nome do comprador: ")
#     valorTotalAcoes = precoAcao * qtdeAcao
#     acoes[0].append(qtdeAcao)
#     acoes[1].append(precoAcao)
#     acoes[2].append(nomeComprador)
#     acoes[3].append(valorTotalAcoes)
#     cont+=1

# Input de dados a partir do arquivo baseAcoes.txt
with open("baseAcoes.txt", "r") as arquivo:
    quantidades = eval(arquivo.readline())
    precos = eval(arquivo.readline())
    nomes = eval(arquivo.readline())
    valorTotalAcoes = eval(arquivo.readline())
    
acoes = [quantidades, precos, nomes, valorTotalAcoes]
    
    
patrimonios = [[0 for nome in list(set(acoes[2]))], list(set(acoes[2]))]

contPatrimonios = 0
contAcoes = 0
while contPatrimonios < len(patrimonios[1]):
    while contAcoes < len(acoes[2]):
        if patrimonios[1][contPatrimonios] == acoes[2][contAcoes]:
            patrimonios[0][contPatrimonios] += acoes[3][contAcoes]
        contAcoes+=1
    contPatrimonios+=1
    contAcoes=0


# backup
# contadorNomes = [[acoes[3].count(nome) for nome in set(acoes[2])], list(set(acoes[2]))] #[[quantidadeAparicoes], [nome]]


print("\nTabela de patrimônios")
print("---------------------")
cont = 0
while cont < len(patrimonios[1]):
    print(f"Patrimônio: {patrimonios[0][cont]:.2f}, nome: {patrimonios[1][cont]}")
    cont+=1
    
with open("arrayEx6.txt", "w") as arquivo:
    arquivo.write(str(patrimonios))