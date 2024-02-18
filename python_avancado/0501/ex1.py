class Aluno ():
    def __init__ (self, nome, serie):
        self.nome = nome
        self.serie = serie
        self.materiais = []
        
    def adicionar_material(self, material):
        self.materiais.append(material)
        

class Material ():
    def __init__ (self, nome, tipo):
        self.nome = nome
        self.tipo = tipo
        
joao = Aluno('joao', '8ª série')
joao.adicionar_material(Material('Caneta Azul', 'BIC Esferográfica'))

print(joao.materiais[0])
print(joao.materiais[0].nome)
print(joao.materiais[0].tipo)