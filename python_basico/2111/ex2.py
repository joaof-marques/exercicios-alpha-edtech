import csv

produtos_disponiveis = []

with open("outputEx1.csv", "r", encoding='utf-8') as arquivo:
    tabela = csv.reader(arquivo, delimiter=';')
    for i in tabela:
        produtos_disponiveis.append((i[0], int(i[1]), int(i[2]), float(i[3])))

print("\nProdutos cadastrados no estoque:\n")
for i in produtos_disponiveis:
    print(f"Nome: {i[0]}\t|\tCódigo: {i[1]}\t|\tQuantidade em estoque: {i[2]}\t|\tPreço: R$ {i[3]:.2f}")