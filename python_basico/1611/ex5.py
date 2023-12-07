import statistics

# Input de dados manual
# numeroAcoes = int(input("Insira o tamanho do array de ações: "))

# acoes = [[],[]] #[[quantidade], [preco]]
# cont = 0

# #alimentar o banco de dados de ações
# while cont < numeroAcoes:
#     qtdeAcao = int(input(f"Insira a quantidade da ação {cont+1}: "))
#     precoAcao = float(input(f"Insira ao preço da ação {cont+1}: ").replace(",", "."))
#     acoes[0].append(qtdeAcao)
#     acoes[1].append(precoAcao)
#     cont+=1

# Input de dados a partir do arquivo baseAcoes.txt
with open("baseAcoes.txt", "r") as arquivo:
    quantidades = eval(arquivo.readline())
    precos = eval(arquivo.readline())
    nomes = eval(arquivo.readline())
    valorTotalAcoes = eval(arquivo.readline())
    
acoes = [quantidades, precos, nomes, valorTotalAcoes]

cont = 0
header = ["Estatísticas das quantidades de ações", "Estatísticas does preços das ações"]
while cont < 2:
    print()
    print(header[cont])
    print(f"{'-'*len(header[cont])}")
    media = statistics.mean(acoes[cont])
    mediana = statistics.median(acoes[cont])
    minimo = min(acoes[cont])
    maximo = max(acoes[cont])
    amplitude = maximo - minimo
    primeiros5elementos = acoes[cont][0:5]
    ultimos5elementos = acoes[cont][len(acoes[cont])-5:len(acoes[cont])]
    desvioPadrao = statistics.pstdev(acoes[cont])
    variancia = statistics.pvariance(acoes[cont])

    print(f"Média: {media:.2f}\tDefinição: Valor médio dos elementos do vetor.")
    print(f"mediana: {mediana:.2f}, \tDefinição: Valor central quando os elementos estão ordenados.")
    print(f"minimo: {minimo}, \tDefinição: Menor valor no vetor.")
    print(f"maximo: {maximo}, \tDefinição: Maior valor no vetor.")
    print(f"amplitude: {amplitude}, \tDefinição: Diferença entre máximo e mínimo.")
    print(f"primeiros5elementos: {primeiros5elementos}, \tDefinição: Os cinco primeiros valores no vetor.")
    print(f"ultimos5elementos: {ultimos5elementos}, \tDefinição: Os cinco últimos valores no vetor.")
    print(f"desvioPadrao: {desvioPadrao:.2f}, \tDefinição: Medida de dispersão dos dados.")
    print(f"variancia: {variancia:.2f}, \tDefinição: Média dos quadrados das diferenças em relação à média.")
    print("\n")
    cont+=1