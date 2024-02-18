class SenhaFracaError(Exception):
    def __init__(self, mensagem="A senha não atende os requisitos. Tente novamente."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

def valida_senha (senha:str) -> bool:
    if len(senha)<8 or not any(caractere in senha for caractere in "!@#$%*()[]?/"):
        return False
    
    return True
    
senha = input("Insira uma senha: ")

try:
    if not valida_senha(senha):
        raise SenhaFracaError
    print("Senha validada com sucesso!")
except SenhaFracaError as error:
    print(error.mensagem)