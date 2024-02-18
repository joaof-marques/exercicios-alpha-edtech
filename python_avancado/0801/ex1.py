class Carro:
    def __init__ (self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    def __str__(self) -> str:
        return f'Nome do carro: {self.nome}'
    
gol = Carro(nome = "Gol Bola", ano = 1995, cor = "Branco")
uno = Carro(nome = "uno", cor = "Prata", escada = True)

for carro in [gol, uno]:
    print(f"------ Atributos do {carro.nome} ------")
    for key, value in carro.__dict__.items():
        print(f"{key}: {value}")


