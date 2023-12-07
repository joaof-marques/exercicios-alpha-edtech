numMaior = 0
alturaMaior = 0
numMenor = 0
alturaMenor = 999

for i in range(10):
    numAluno = int(input(f"{i}:Insira o número do aluno: "))
    alturaAluno = int(input(f"{i}:Insira a altura do aluno: "))
    
    if alturaAluno > alturaMaior:
        numMaior = numAluno
        alturaMaior = alturaAluno
    if alturaAluno < alturaMenor:
        numMenor = numAluno
        alturaMenor = alturaAluno
        
print(f"O maior aluno é o {numMaior}, medindo {alturaMaior} cm")
print(f"O menor aluno é o {numMenor}, medindo {alturaMenor} cm")
