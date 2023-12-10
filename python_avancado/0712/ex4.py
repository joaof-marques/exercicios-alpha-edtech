from typing import List

class Aluno:
    def __init__(self, nome: str, altura: float, idade: int):
        self.nome = nome
        self.altura = altura
        self.idade = idade

def calcula_media_idade(alunos: List[Aluno]):
    totalIdade = sum(aluno.idade for aluno in alunos)
    return totalIdade/len(alunos)

alunos: List[Aluno] = [
    Aluno("João", 1.80, 28),
    Aluno("Jeane", 1.65, 28),
    Aluno("Geovana", 1.59, 23),
    Aluno("Gabriela", 1.70, 23),
    {"Michael", 1.8, 25}
]

mediaIdades = calcula_media_idade(alunos)
print(f"A média das idades é {mediaIdades}")