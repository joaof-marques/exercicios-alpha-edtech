tamanho = int(input("Insira o tamanho do tabuleiro: "))

linha = 0
aux = 0

while linha < tamanho:
    coluna = 0        
    while coluna < tamanho:
        if (coluna+linha)%2==0:
            print("O", end="")
        else: 
            print("X", end="")
        aux += 1
        coluna+= 1
    print("")
    linha += 1 
