class Animal:
    def __init__(self, nome:str, especie:str, som:str="Som genérico") -> None:
        self.nome = nome
        self.especie = especie
        self.som = som
        
    def apresentar(self):
        print(f"{self.som}! Meu nome é {self.nome} e eu sou um(a) {self.especie}")
        
        
gato = Animal("Jotinha", "Gato", "Miaau")
cachorro = Animal("Toddy", "Cachorro", "AuAu")
raposa = Animal("Fox", "Raposa")

gato.apresentar()
cachorro.apresentar()
raposa.apresentar()