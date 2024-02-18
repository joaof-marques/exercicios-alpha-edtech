class Produto:
    def __init__ (self, nome, preco, fornecedor):
        self.nome = nome
        self.preco = preco
        self.fornecedor = fornecedor
        
    def get_nome(self):
        return self.nome
    
    def get_preco (self):
        return self.preco
    
    def get_fornecedor(self):
        return self.fornecedor
    


class Pedido_venda:
    def __init__(self, cliente, valor_total, produtos=[]):
        self.cliente = cliente
        self.valor_total = valor_total
        self.produtos = produtos
        self.qtde_produtos = len(self.produtos)
        
    def get_valor_total(self):
        return self.valor_total
    
    def get_qtde_produtos(self):
        return self.qtde_produtos
    
feijao = Produto('Feijao Carioca', 6.8, 'Kicaldo')
arroz = Produto('Arroz branco Tipo 1', 20, 'Cristal')
coca_cola = Produto('Cola-Cola', 7, 'Coca-Cola')
chocolate = Produto('Barra Chocolate 350g', 8, 'Garoto')

pedido01 = Pedido_venda('João', 33.8, [feijao, arroz, coca_cola])
pedido02 = Pedido_venda('Paulo Marcotti', 15, [coca_cola, chocolate])
pedido03 = Pedido_venda('Mateus', 41.8, [feijao, arroz, coca_cola, chocolate])

print('Produtos Pedido 01:', pedido01.produtos)
print('Produtos Pedido 02:', pedido02.produtos)
print('Produtos Pedido 03:', pedido03.produtos)