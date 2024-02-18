class Cliente:
    def __init__(self, nome:str, saldo:float) -> None:
        self.nome = nome
        self.saldo = saldo
        
    def __str__(self) -> str:
        return f'Cliente {self.nome}. Saldo atual: R$ {self.saldo}'    
    
    def __del__(self):
        print(f"Cliente {self.nome} deletado.")
        
joao = Cliente('João Marques', 123.32)
marcotti = Cliente('Paulo Marcotti', 999999.99)

print(joao)
print(marcotti)

del joao

#tentantiva de acessar joao depois da deleção
#levanta o erro NameError pois já não existe mais na execução (pode ser tratado com try except)
print(joao)

print(marcotti)