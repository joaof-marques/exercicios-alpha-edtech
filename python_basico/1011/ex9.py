qtdeAlunos = int(input("Informe a quantidade de alunos desejada: "))

numMaior = 0
alturaMaior = 0
numMenor = 0
alturaMenor = 9999
numPesado = 0
pesoPesado = 0
numLeve = 0
pesoLeve = 9999
somaAltura = 0
somaPeso = 0

for i in range(qtdeAlunos):
    numAluno = int(input(f"{i}:Insira o código do aluno: "))
    alturaAluno = int(input(f"{i}:Insira a altura do aluno: "))
    pesoAluno = int(input(f"{i}:Insira o peso do aluno: "))
    somaAltura+=alturaAluno
    somaPeso+= pesoAluno
    
    if alturaAluno > alturaMaior:
        numMaior = numAluno
        alturaMaior = alturaAluno
    elif alturaAluno < alturaMenor:
        numMenor = numAluno
        alturaMenor = alturaAluno
        
    if pesoAluno > pesoPesado:
        numPesado = numAluno
        pesoPesado = pesoAluno
    elif pesoAluno < pesoLeve:
        numLeve = numAluno
        pesoLeve = pesoAluno
        
    
        
print(f"O maior aluno é o {numMaior}, medindo {alturaMaior} cm")
print(f"O menor aluno é o {numMenor}, medindo {alturaMenor} cm")
print(f"O aluno mais pesado é o {numPesado}, pesando {pesoPesado} kgs")
print(f"O aluno mais leve é o {numLeve}, pesando {pesoLeve} kgs")
print(f"A média das alturas é {somaAltura/qtdeAlunos} cm e a média de peso é {somaPeso/qtdeAlunos}")
