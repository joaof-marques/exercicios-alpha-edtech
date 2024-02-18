import os

dict_produtos = {
    1: {
        "tipo_produto": "banana",
        "preco": 5.99
    },
    2: {
        "tipo_produto": "maçã",
        "preco": 7.99
    },
    3: {
        "tipo_produto": "tomate",
        "preco": 9.99
    }
}

class Loja:
    def __init__(self, valor_em_caixa = 0):
        self.valor_em_caixa = valor_em_caixa 
        self.estoque_banana = []
        self.estoque_maca = []
        self.estoque_tomate = []
              
    def inserir_produto_estoque (self, id_produto, quantidade, data):
        novo_produto_estoque = Item_estoque(id_produto, quantidade, data)
        
        match id_produto:
            case 1:
                self.estoque_banana.append(novo_produto_estoque)
                self.atualizar_valor_em_caixa(self.estoque_banana[-1], 1)
                print("Carregamento de bananas inserido no estoque com sucesso!")
                input("\nAperte uma tecla para continuar.")
            case 2:
                self.estoque_maca.append(novo_produto_estoque)
                self.atualizar_valor_em_caixa(self.estoque_maca[-1], 1)
                print("Carregamento de maçã inserido no estoque com sucesso!")
                input("\nAperte uma tecla para continuar.")
            case 3:
                self.estoque_tomate.append(novo_produto_estoque)
                self.atualizar_valor_em_caixa(self.estoque_tomate[-1], 1)
                print("Carregamento de tomate inserido no estoque com sucesso!")
                input("\nAperte uma tecla para continuar.")
            case _:
                print(f"Estoque não existe. Insira um valor entre 1 e {len(dict_produtos.keys())}")
                input("\nAperte uma tecla para continuar.")
        
    def remover_produto_estoque (self, id_produto, quantidade):
        
        if quantidade > 0:
            match id_produto:
                case 1:
                    if len(self.estoque_banana) == 0 or (len(self.estoque_banana) == 1 and quantidade > self.estoque_banana[0].quantidade_estoque):
                        print(f"Não há estoque para o produto selecionado. {quantidade}kgs de banana não puderam ser vendidos")
                        input("\nAperte uma tecla para continuar.")
                    elif quantidade >= self.estoque_banana[-1].quantidade_estoque:
                        quantidade -= self.estoque_banana[-1].quantidade_estoque
                        self.atualizar_valor_em_caixa(self.estoque_banana[-1], 2, 1/10)
                        self.estoque_banana = self.estoque_banana[1:]
                        if quantidade == 0:
                            print(f"Venda efetuada com sucesso!\nValor total em caixa: R$ {self.valor_em_caixa:.2f}")
                            input("\nAperte uma tecla para continuar.")
                            return
                        self.remover_produto_estoque(id_produto, quantidade)
                        
                    elif quantidade < self.estoque_banana[-1].quantidade_estoque:
                        self.estoque_banana[-1].quantidade_estoque -= quantidade
                        self.estoque_banana[-1].valor_em_estoque = self.estoque_banana[-1].quantidade_estoque * self.estoque_banana[-1].produto['preco']
                        self.atualizar_valor_em_caixa(self.estoque_banana[-1], 2, 1/10)
                        
                case 2:
                    if len(self.estoque_maca) == 0 or (len(self.estoque_maca) == 1 and quantidade > self.estoque_maca[0].quantidade_estoque):
                        print(f"Não há estoque para o produto selecionado. {quantidade}kgs de maçã não puderam ser vendidos")
                        input("\nAperte uma tecla para continuar.")
                    elif quantidade >= self.estoque_maca[-1].quantidade_estoque:
                        quantidade -= self.estoque_maca[-1].quantidade_estoque
                        self.atualizar_valor_em_caixa(self.estoque_maca[-1], 2, 1/10)
                        self.estoque_maca = self.estoque_maca[1:]
                        self.remover_produto_estoque(id_produto, quantidade)
                    elif quantidade < self.estoque_maca[-1].quantidade_estoque:
                        self.estoque_maca[-1].quantidade_estoque -= quantidade
                        self.estoque_maca[-1].valor_em_estoque = self.estoque_maca[-1].quantidade_estoque * self.estoque_maca[-1].produto['preco']
                        self.atualizar_valor_em_caixa(self.estoque_maca[-1], 2, 1/10)
                case 3:
                    if len(self.estoque_tomate) == 0 or (len(self.estoque_tomate) == 1 and quantidade > self.estoque_tomate[0].quantidade_estoque):
                        print(f"Não há estoque para o produto selecionado. {quantidade}kgs de tomate não puderam ser vendidos")
                        input("\nAperte uma tecla para continuar.")
                    elif quantidade >= self.estoque_tomate[-1].quantidade_estoque:
                        quantidade -= self.estoque_tomate[-1].quantidade_estoque
                        self.atualizar_valor_em_caixa(self.estoque_tomate[-1], 2, 1/10)
                        self.estoque_tomate = self.estoque_tomate[1:]
                        self.remover_produto_estoque(id_produto, quantidade)
                    elif quantidade < self.estoque_tomate[-1].quantidade_estoque:
                        self.estoque_tomate[-1].quantidade_estoque -= quantidade
                        self.estoque_tomate[-1].valor_em_estoque = self.estoque_tomate[-1].quantidade_estoque * self.estoque_tomate[-1].produto['preco']
                        self.atualizar_valor_em_caixa(self.estoque_tomate[-1], 2, 1/10)
                case _:
                    print(f"Estoque não existe. Insira um valor entre 1 e {len(dict_produtos.keys())}") 
                    
        else: return
        
    def atualizar_valor_em_caixa(self, novo_produto_estoque, operador:int, comissao_operacao=0):
        self.valor_em_caixa = self.valor_em_caixa + (((-1)**operador)*novo_produto_estoque.valor_em_estoque*(1+comissao_operacao))
        
    def listar_estoque(self):
        os.system("clear")
        print("----- Estoque de Bananas -----")
        for item_estoque in self.estoque_banana:
            print(item_estoque)
        print("\n")
        print("----- Estoque de Maçãs -----")
        for item_estoque in self.estoque_maca:
            print(item_estoque)
        print("\n")
        print("----- Estoque de Tomates -----")
        for item_estoque in self.estoque_tomate:
            print(item_estoque)
            
        print(f"\n\nValor total em caixa: R$ {self.valor_em_caixa:.2f}")
        input("\nAperte uma tecla para continuar.")
        



class Item_estoque:
    def __init__(self, id_produto, quantidade_estoque, data_entrada_estoque):
        self.produto = dict_produtos[id_produto]
        self.id_produto = id_produto
        self.quantidade_estoque = quantidade_estoque
        self.data_entrada_estoque = data_entrada_estoque
        self.valor_em_estoque = float(quantidade_estoque) * self.produto["preco"]

    def __str__(self):
        return f"Data do Carregamento: {self.data_entrada_estoque}\t|\tQuantidade em estoque: {self.quantidade_estoque} kg\t|\tValor em estoque: R$ {self.valor_em_estoque:.2f}"


def imprimir_menu():
    os.system("clear")
    print("----- Menu de seleção -----")
    print("1 - Cadastrar entrada de item no estoque (abastecimento)\n2 - Cadastrar saída de item no estoque (venda de produto)\n3 - Listar items em estoque\n4 - Sair")
    opcao = int(input("Opção desejada: "))
    return opcao
    

if __name__ == "__main__":
    loja = Loja()
    while True:
        opcao = imprimir_menu()
        match opcao:
            case 1:
                os.system("clear")
                print("----- Cadastrar entrada de item no estoque (abastecimento) -----")
                id = int(input("Insira o id do produto: "))
                qtde = int(input("Insira a quantidade do produto: "))
                data = input("Insira a data (dd/mm/aaaa) de entrada do produto no estoque: ")
                
                loja.inserir_produto_estoque(id, qtde, data)   
            case 2: 
                os.system("clear")
                print("----- Cadastrar saída de item no estoque (venda de produto) -----")
                id = int(input("Insira o id do produto: "))
                qtde = int(input("Insira a quantidade do produto: "))
                loja.remover_produto_estoque(id, qtde)
            case 3:
                loja.listar_estoque()
            case 4:
                break
            case _:
                print("Opção inválida. Tente novamente")
                input("\nAperte uma tecla para continuar.")