class Cliente:
    def __init__(self, nome, cadastrado):
        self.nome = nome
        self.cadastrado = cadastrado
        self.pedidos = []
        
    def get_nome(self):
        return self.nome

    def registrar_pedido(self, pedido):
        self.pedidos.append(pedido)

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


joao = Cliente('João Marques', False)
pmarcotti = Cliente('Paulo Marcotti', True)


pedido01 = Pedido_venda('João Marques', 33.8, [feijao, arroz, coca_cola])
joao.registrar_pedido(pedido01)

pedido02 = Pedido_venda('Paulo Marcotti', 15, [coca_cola, chocolate])
pmarcotti.registrar_pedido(pedido02)

pedido03 = Pedido_venda('João Marques', 41.8, [feijao, arroz, coca_cola, chocolate])
joao.registrar_pedido(pedido03)

pedido04 = Pedido_venda('Anônimo', 7, [coca_cola])

print('----- Pedidos João Marques -----')
for num, pedido in enumerate(joao.pedidos):
    print(f'------- Pedido {num+1} -------')
    for produto in pedido.produtos:
        print(produto.get_nome())

print('\n') 
print('----- Pedidos Paulo Marcotti -----')
for num, pedido in enumerate(pmarcotti.pedidos):
    print(f'------- Pedido {num+1} -------')
    for produto in pedido.produtos:
        print(produto.get_nome())
    