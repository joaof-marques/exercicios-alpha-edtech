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
    def __init__(self, cliente, valor_total, produtos=[], id=''):
        self.cliente = cliente
        self.valor_total = valor_total
        self.produtos = produtos
        self.qtde_produtos = len(self.produtos)
        self.id = id
        
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


pedido01 = Pedido_venda('João Marques', 33.8, [feijao, arroz, coca_cola], 'pedido01')
joao.registrar_pedido(pedido01)

pedido02 = Pedido_venda('Paulo Marcotti', 15, [coca_cola, chocolate], 'pedido02')
pmarcotti.registrar_pedido(pedido02)

pedido03 = Pedido_venda('João Marques', 41.8, [feijao, arroz, coca_cola, chocolate], 'pedido03')
joao.registrar_pedido(pedido03)

pedido04 = Pedido_venda('Anônimo', 7, [coca_cola], 'pedido04')

pedidos = [pedido01, pedido02, pedido03, pedido04]
produtos_cadastrados = [feijao, arroz, coca_cola, chocolate]

for produto_cadastrado in produtos_cadastrados:
    pedido_selecionado = []
    for pedido in pedidos:
        for produto in pedido.produtos:
            if produto_cadastrado.nome == produto.nome:
                pedido_selecionado.append(pedido.id)
                break
    print(f"{produto_cadastrado.nome}: {', '.join(pedido_selecionado)}")
        

    