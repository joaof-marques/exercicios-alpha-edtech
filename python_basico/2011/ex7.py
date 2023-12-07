#para este exercício estou considerando que o array recebido é do seguinte formato:
#produtos_vendidos = [[produtos], [quantidades]]

produtos_vendidos = [
    ['Caneca', 'Caneta', 'Caderno', 'Caneta', 'Borracha', 'Mouse', 'Teclado', 'Controle Video-Game', 'Caderno', 'Caneta', 'Caneca'],
    [10, 2, 18, 4, 3, 200, 180, 350, 20, 5, 12]
]

produtos_unicos = [list(set(produtos_vendidos[0])),[0 for produto in set(produtos_vendidos[0])]]


for i, produtoUnico in enumerate(produtos_unicos[0]):
    for j, produtoVendido in enumerate(produtos_vendidos[0]):
        
        if produtoUnico == produtoVendido:
            produtos_unicos[1][i]+=1
            
print(produtos_unicos)