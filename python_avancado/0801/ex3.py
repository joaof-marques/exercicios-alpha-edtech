class Cliente:
    def __init__(self, nome:str, saldo:float) -> None:
        self.nome = nome
        self.saldo = saldo
        
    @classmethod
    def cliente_prime(cls, nome:str, saldo:float, limite_credito):
        cliente_prime = cls(nome, saldo)
        cliente_prime.limite_credito = limite_credito
        return cliente_prime
        
    def __str__(self) -> str:
        return f'Cliente {self.nome}. Saldo atual: R$ {self.saldo}'    
    
    def __del__(self):
        print(f"Cliente {self.nome} deletado.")
        
joao = Cliente('João Marques', 123.32)
marcotti = Cliente.cliente_prime('Paulo Marcotti', 50000, 400000)


#Se tentarmos imprimir o limite de credito do joao vamos obter um erro do tipo AttributeError, pois estamos tentando acessar um atributo que só existe para objetos instanciados pelo método construtor alternativo 
# print(joao.limite_credito)
# print(marcotti.limite_credito)
