import csv
import os

produtos_disponiveis = []

produtosACadastrar = int(input("Insira a quantidade de itens a serem cadastados: "))

for i in range(produtosACadastrar):
    os.system('clear')
    nomeNovoProduto = input(f"Insira o nome do produto {i+1}: ")
    codigoNovoProduto = input(f"Insira o código do produto {i+1}: ")
    qtdeNovoProduto = int(input(f"Insira a quantidade do produto {i+1}: "))
    precoNovoProduto = float(input(f"Insira o preço do produto {i+1}: "))

    produtos_disponiveis.append((nomeNovoProduto, codigoNovoProduto, qtdeNovoProduto, precoNovoProduto))

print("\nProdutos cadastrados no estoque:\n")
for i in produtos_disponiveis:
    print(f"Nome: {i[0]}\t|\tCódigo: {i[1]}\t|\tQuantidade em estoque: {i[2]}\t|\tPreço: R$ {i[3]:.2f}")
    
with open("outputEx1.csv", "w", newline='', encoding='utf-8') as arquivo:
    writer = csv.writer(arquivo, delimiter=';')
    for i in produtos_disponiveis:
        writer.writerow(i)
    arquivo.close()