class Documento:
    def __init__(self, nome_arquivo, modo) -> None:
        self.nome_arquivo = nome_arquivo
        self.modo = modo
        self.arquivo = open(nome_arquivo, modo)
        if modo == 'r':
            self.conteudo = self.arquivo.read()
        
    def escrever(self, conteudo):
        if self.modo != 'r':
            self.arquivo.write(conteudo)
        else: print("Não é possível sobrescrever. Arquivo aberto no modo somente leitura")
        
    def fechar_arquivo(self):
        self.arquivo.close()
        print("Arquivo fechado com sucesso")
        
    def __del__(self):
        self.arquivo.close()
        
        
testetxt = Documento('teste.txt', 'r')

print(testetxt.conteudo)

# testetxt.escrever('Documento apagado e reescrito')