class IdadeInvalidaError (ValueError):
    def __init__(self, mensagem="Idade inválida. Favor informar um valor entre 0 e 150."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)


def valida_idade(idade):
    if idade < 0 or idade > 150:
        raise IdadeInvalidaError
    
    print("Idade válida!")
    
    
try:
    valida_idade(240)
except IdadeInvalidaError as erro:
    print(erro.mensagem)