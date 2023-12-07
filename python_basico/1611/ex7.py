with open("arrayEx6.txt", "r") as arquivo:
    conteudoArquivo = arquivo.read()
    dados = eval(conteudoArquivo)
    
    
cont = 0
mudouArray = False
while cont < 4:
    for i in range(len(dados[0])):
        
        if cont == len(dados[0])-1:
            cont = 0
            break
        if dados[0][cont]<dados[0][cont+1]:
            aux = dados[0][cont+1]
            dados[0][cont+1] = dados[0][cont]
            dados[0][cont] = aux
            
            aux = dados[1][cont+1]
            dados[1][cont+1] = dados[1][cont]
            dados[1][cont] = aux
            
            mudouArray = True
        cont+=1
        
    if not mudouArray:
        break
    mudouArray = False
    

melhores3 = [dados[0][0:3],dados[1][0:3]]
piores3 = [dados[0][len(dados)-3:],dados[1][len(dados)-3:]]

tabela = ["Melhores 3:", "Piores 3:"]
separador = [f"{'-'*len(tabela[0])}", f"{'-'*len(tabela[1])}"]

cont1 = 0
cont2 = 0
while cont1 < 2:
    print(tabela[cont1])
    print(separador[cont1])
    while cont2 < 3: 
        if cont1 == 1: cursor = len(dados[0]) - cont2 -1
        else: cursor = cont2
        print(f"Nome: {dados[1][cursor]}  |  Patrimônio Aplicado: R$ {dados[0][cursor]:.2f}")
        cont2+=1
    print()
    cont1+=1
    cont2=0
