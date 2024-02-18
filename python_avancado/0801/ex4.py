class Inimigo:
    def __init__(self, nome:str, vida:float, dano: int) -> None:
        self.nome = nome
        self.vida = vida
        self.dano = dano
    
    def __del__(self):
        print(f"Inimigo {self.nome} derrotado!")
    
    def atualiza_vida(self, dano_recebido):
        self.vida -= dano_recebido #deduz o dano da vida
        if self.vida <= 0:
            self.__del__() #monstro morreu = pode ser deletado da memória
  
class Heroi:
    def __init__(self, nome:str, vida:float, dano: int) -> None:
        self.nome = nome
        self.vida = vida
        self.dano = dano
    
    def __del__(self):
        print(f"O herói foi derrotado! Você Perdeu!")
    
    def atualiza_vida(self, dano_recebido):
        self.vida -= dano_recebido #deduz o dano da vida
        if self.vida <= 0:
            self.__del__() #heroi morreu = pode ser deletado da memória
          
heroi = Heroi('João', 500, 100)
ciclope = Inimigo('Ciclope com clava de madeira', 300, 50)


while heroi.vida>0 and ciclope.vida>0:
    ciclope.atualiza_vida(heroi.dano)
    heroi.atualiza_vida(ciclope.dano)


print('----------- FIM DA BATALHA ÉPICA ----------- ')
