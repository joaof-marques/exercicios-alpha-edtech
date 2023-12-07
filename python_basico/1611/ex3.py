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
ultimos5elementos = dados[-5:]
desvioPadrao = statistics.pstdev(dados)
variancia = statistics.pvariance(dados)


print(f"Média: {media:.2f}\t\tDefinição: Valor médio dos elementos do vetor.")
print(f"mediana: {mediana:.2f}, \t\tDefinição: Valor central quando os elementos estão ordenados.")
print(f"minimo: {minimo}, \t\tDefinição: Menor valor no vetor.")
print(f"maximo: {maximo}, \t\tDefinição: Maior valor no vetor.")
print(f"amplitude: {amplitude}, \t\tDefinição: Diferença entre máximo e mínimo.")
print(f"primeiros5elementos: {primeiros5elementos}, \t\tDefinição: Os cinco primeiros valores no vetor.")
print(f"ultimos5elementos: {ultimos5elementos}, \t\tDefinição: Os cinco últimos valores no vetor.")
print(f"desvioPadrao: {desvioPadrao:.2f}, \t\tDefinição: Medida de dispersão dos dados.")
print(f"variancia: {variancia:.2f}, \t\tDefinição: Média dos quadrados das diferenças em relação à média.")