class Pessoa ():
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade
        
    def __hash__(self):
        return hash(self.nome)
    
    def atributes(self):
        return f"Nome: {self.nome}, idade: {self.idade}"

joao = Pessoa('joao', 28)
jeane = Pessoa('jeane', 29)
gabriel = Pessoa('gabriel', 30)
geovana = Pessoa('geovana', 31)
gabriela = Pessoa('gabriela', 32)

dict_pessoas = { pessoa.__hash__() : pessoa for pessoa in [joao, jeane, gabriel, geovana, gabriela] }

opcao = input("Insira o nome da pessoa a obter os dados: ")
print(dict_pessoas[hash(opcao)].atributes())


