import pprint, os

class SistemaRastreamento:
    def __init__(self):
        self.pedidos = {}
        self.quantidade_pedidos = 0
        self.limite_hashs = 100
        
        
    def adicionar_pedido(self, codigo, status = "Recebido"):
        
        hash_codigo = self.gerar_hash(codigo)
        
        if hash_codigo in self.pedidos:
            print(f"Código de rastreamento {codigo} já existe.")
        else:
            self.pedidos[hash_codigo] = {'codigo':codigo, 'status': status}
            self.quantidade_pedidos += 1 
            print(f"Pedido {codigo} adicionado com status: {status}.")

    def atualizar_status(self, codigo, status):
        
        hash_codigo = self.gerar_hash(codigo)
        
        if hash_codigo in self.pedidos:
            self.pedidos[hash_codigo]['status'] = status
            print(f"Status do pedido {codigo} atualizado para: {status}.")
        else:
            print(f"Pedido com código {codigo} não encontrado.")

    def consultar_status(self, codigo):        
        hash_codigo = self.gerar_hash(codigo)
                
        if hash_codigo in self.pedidos and self.pedidos[hash_codigo]['codigo'] == codigo:
            print(self.pedidos[hash_codigo])
            return 
        else:
            print(f"O código {codigo} não foi encontrado.")
        # return self.pedidos.get(hash_codigo, "Pedido não encontrado.")
    
    def gerar_hash(self, codigo):
        codigo_numerico = codigo[2:11]
        hash = 0
        try:
            for _ in range(len(codigo_numerico)-1):
                hash += (_*int(codigo_numerico[_]))
        except ValueError:
            os.system("clear")
            print("O código informado não está no formato padrão AA000000000BB")
            input("Aperte uma tecla para proseguir...\n")
            return
        return hash % self.limite_hashs
    
    def verifica_capacidade_hashmap(self):
        if self.quantidade_pedidos >= self.limite_hashs*0.7:
            print("É necessário fazer um rehashing")
            return
            
        print(f"A ocupação atual do hashmap é {self.quantidade_pedidos}")
    
    def listar_pedidos_cadastrados(self):
        pprint.pprint(self.pedidos)

# # Exemplo de uso

# sistema.atualizar_status("AA102938475BR", "Em processamento")
# print(sistema.consultar_status("AA102938475BR"))  # Deve exibir "Em processamento"
# sistema.verifica_capacidade_hashmap()
# sistema.listar_pedidos_cadastrados()

# print(sistema.gerar_hash('AA102938475BR'))

if __name__ == "__main__":
    sistema = SistemaRastreamento()
    
    sistema.adicionar_pedido("AA102938475BR", "Recebido")
    sistema.adicionar_pedido("BB572916384BR", "Recebido")
    sistema.adicionar_pedido("CC209384715BR", "Recebido")
    sistema.adicionar_pedido("DD839201746BR", "Recebido")
    sistema.adicionar_pedido("EE612094837BR", "Recebido")
    # sistema.adicionar_pedido("FF304857192BR", "Recebido")
    sistema.adicionar_pedido("GG958162734BR", "Recebido")
    sistema.adicionar_pedido("HH485710293BR", "Recebido")
    
    while True:
        os.system("clear")
        opcao = int(input("Escolha uma opção:\n1 - Cadastrar pedido\n2 - Atualizar status de pedido\n3 - Consultar status de pedido único\n4 - Listar todos os pedidos cadastrados\n5 - Verificar capacidade do hashmap\n6 - Sair\n"))
        
        
        match opcao:
            case 1:
                os.system("clear")
                codigo = input("Insira um código de rastreio (Formato AA000000000BB): \n")
                sistema.adicionar_pedido(codigo)
                input("Aperte uma tecla para proseguir...\n")
            case 2:
                os.system("clear")
                codigo = input("Insira o código do pedido a ser alterado (Formato AA000000000BB): \n")
                status = input("Insira o novo status do pedido a ser alterado: \n")
                sistema.atualizar_status(codigo, status)
                input("Aperte uma tecla para proseguir...\n")
            case 3:
                os.system("clear")
                codigo = input("Insira o código do pedido a ser consultado (Formato AA000000000BB): \n")
                sistema.consultar_status(codigo)
                input("Aperte uma tecla para proseguir...\n")
            case 4:
                os.system("clear")
                sistema.listar_pedidos_cadastrados()
                input("Aperte uma tecla para proseguir...\n")
            case 5:
                os.system("clear")
                sistema.verifica_capacidade_hashmap()
                input("Aperte uma tecla para proseguir...\n")            
            case 6:
                break                      
            case _:
                os.system("clear")
                print("Opção inválida.")
                input("Aperte uma tecla para proseguir...\n")
                