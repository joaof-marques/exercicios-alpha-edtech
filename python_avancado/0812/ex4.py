class Animal:
    def __init__(self, nome:str, especie:str, caracteristica:str, pele:str, som:str="Som genérico") -> None:
        self.nome = nome
        self.especie = especie
        self.caracteristica = caracteristica
        self.pele = pele
        self.som = som
        
    def apresentar(self):
        print(f"{self.som}! Meu nome é {self.nome} e eu sou um(a) {self.especie}")
        
        
gato = Animal("Jotinha", "Gato", "Mamífero", "Pelos limpinhos", "Miaau")
cachorro = Animal("Toddy", "Cachorro", "Mamífero", "Pelos bagunçados", "AuAu")
raposa = Animal("Fox", "Raposa", "Mamífero", "Pelos com terra")

gato.apresentar()
cachorro.apresentar()
raposa.apresentar()