import statistics

with open("arrayEx2.txt", "r") as arquivo:
    conteudoArquivo = arquivo.read()
    dados = eval(conteudoArquivo)
    
media = statistics.mean(dados)
mediana = statistics.median(dados)
minimo = min(dados)
maximo = max(dados)
amplitude = maximo - minimo
primeiros5elementos = dados[0:5]
ultimos5elementos = dados[len(dados)-5:len(dados)]
desvioPadrao = statistics.pstdev(dados)
variancia = statistics.pvariance(dados)

dadosSemOutliers = [x for x in dados if not(x > media + (2*desvioPadrao) or x < media - (2*desvioPadrao))]


print(f"Média: {media:.2f}\tDefinição: Valor médio dos elementos do vetor.")
print(f"mediana: {mediana:.2f}, \tDefinição: Valor central quando os elementos estão ordenados.")
print(f"minimo: {minimo}, \tDefinição: Menor valor no vetor.")
print(f"maximo: {maximo}, \tDefinição: Maior valor no vetor.")
print(f"amplitude: {amplitude}, \tDefinição: Diferença entre máximo e mínimo.")
print(f"primeiros5elementos: {primeiros5elementos}, \tDefinição: Os cinco primeiros valores no vetor.")
print(f"ultimos5elementos: {ultimos5elementos}, \tDefinição: Os cinco últimos valores no vetor.")
print(f"desvioPadrao: {desvioPadrao:.2f}, \tDefinição: Medida de dispersão dos dados.")
print(f"variancia: {variancia:.2f}, \tDefinição: Média dos quadrados das diferenças em relação à média.")

with open("arrayEx4.txt", "w") as arquivo:
    arquivo.write(str(dadosSemOutliers))