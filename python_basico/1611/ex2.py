with open("arrayEx1.txt", "r") as arquivo:
    conteudoArquivo = arquivo.read()
    conteudoArquivo = conteudoArquivo.replace("[", "")
    conteudoArquivo = conteudoArquivo.replace("]", "")
    dados = conteudoArquivo.split(", ")

cont, soma, media, maior, valoresValidosMedia = 0,0,0,0,0
menor = 999999999
maior = int(dados[0])



while cont < len(dados):
    dados[cont] = int(dados[cont])
    
    if dados[cont] > 0:
        if dados[cont] > maior:
            maior = dados[cont]
        elif dados[cont]<menor:
            menor = dados[cont]
            
        soma += dados[cont]
        valoresValidosMedia += 1
        
    cont+=1        
media = round(soma/valoresValidosMedia, 2)
    
cont = 0
while cont < len(dados):
    if dados[cont] <= 0:
        dados[cont] = media 
    
    cont += 1

primeiros5valores = dados[0:5]
ultimos5valores = dados[-5:]

print("soma:", soma)
print("media:", media)
print("primeiros5valores:", primeiros5valores)
print("ultimos5valores:", ultimos5valores)
print("Maior valor:", maior)
print("Menor valor:", menor)
print("Vetor dados:", dados)

with open("arrayEx2.txt", "w") as arquivo:
    arquivo.write(str(dados))