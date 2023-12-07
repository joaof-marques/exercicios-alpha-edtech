import csv
import os

produtos_disponiveis = []

with open("outputEx1.csv", "r", encoding='utf-8') as arquivo:
    tabela = csv.reader(arquivo, delimiter=';')
    for i in tabela:
        produtos_disponiveis.append((i[0], int(i[1]), int(i[2]), float(i[3])))

opcao = '1'
dadosAlterados = False
while opcao in ['1', '2']:
    os.system('clear')
    opcao = input("Informe a opção desejada:\n1 - Alterar quantidade de um produto\n2 - Exibir produtos em estoque\nDigite qualquer outra opção para encerrar o programa\n")
    
    if opcao == '1':
        os.system('clear')
        print("\n - - - Alterar quantidade de produto cadastrado - - - \n")
        novaQuantidade = ''
        codigoProduto = int(input("Informe o código do produto cadastrado: "))
        for i in range(len(produtos_disponiveis)):
            if produtos_disponiveis[i][1] == codigoProduto:
                novaQuantidade = int(input("Insira a nova quantidade do produto: "))
                produtos_disponiveis[i] = (produtos_disponiveis[i][0], produtos_disponiveis[i][1], novaQuantidade, produtos_disponiveis[i][3])
                dadosAlterados = True
                print("\nQuantidade de produtos alterada com sucesso.\n")
        if not novaQuantidade:
            print("\nCódigo de produto não cadastrado. Tente novamente\n")
            
    elif opcao == '2':
        os.system('clear')
        print("\nProdutos cadastrados no estoque:\n")
        for i in produtos_disponiveis:
            print(f"Nome: {i[0]}\t|\tCódigo: {i[1]}\t|\tQuantidade em estoque: {i[2]}\t|\tPreço: R$ {i[3]:.2f}")
    else: break
            
    input("Pressione uma tecla para continuar")
    
if dadosAlterados:
    with open("outputEx1.csv", "w", newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo, delimiter=';')
        for i in produtos_disponiveis:
            writer.writerow(i)
        arquivo.close()
            