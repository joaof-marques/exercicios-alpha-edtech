nome = input("Insira o nome do aluno: ")
media = float(input("Insira a média do aluno: "))

def processaAluno (**kwargs):
    kwargs["situacao"] = "Aprovado" if kwargs["media"]>7 else "Reprovado"
    return kwargs

print(processaAluno(nome = nome, media = media))