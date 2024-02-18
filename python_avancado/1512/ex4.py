class ArquivoVazio(Exception):
    def __init__(self, mensagem="O arquivo está vazio"):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

def le_arquivo(nome_arquivo:str) -> None:
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
           
            if len(conteudo)==0:
               raise ArquivoVazio
           
            print(conteudo)

    except FileNotFoundError as erro:
        print("Arquivo não encontrado, tente novamente com outro nome")

    except PermissionError as erro:
        print("Você não tem permissão para acessar/modificar o arquivo.")
    except ArquivoVazio as erro:
        print(erro.mensagem)



arquivo:str = input("Insira o arquivo a ser aberto (informar com extensão)")
le_arquivo(arquivo)