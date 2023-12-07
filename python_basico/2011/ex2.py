cores = ['amarelou', 'vermelhou', 'azulou', 'medrou', 'burrou']
misturas2a2, misturas3a3, misturas4a4 = [], [], []

misturas2a2 = [['laranjou', 'amarelou', 'vermelhou'], ['verdou', 'amarelou', 'azulou'], ['amedrou', 'amarelou', 'medrou'], ['aburrou', 'amarelou', 'burrou'], ['roxou', 'vermelhou', 'azulou'], ['verdrou', 'vermelhou', 'medrou'], ['verburrou', 'vermelhou', 'burrou'], ['azudrou', 'azulou', 'medrou'], ['azurrou', 'azulou', 'burrou'], ['merrou', 'medrou', 'burrou']]

contadorPrimaria = 1

# Input manual dos nomes das cores secundárias. Basta descomentar o código abaixo e comentar a linha 4 acima e vai ser possível inserir os nomes manualmente
# print("\nCombinações 2 a 2:\n")
# for posCor1, cor1 in enumerate(cores):
#     for posCor2, cor2 in enumerate(cores):
#         if posCor2 <= posCor1: continue
#         misturas2a2.append([input(f"Qual a cor resultante da mistura {cor1} e {cor2}? "), cor1, cor2])

print(f"\nAs cores secundárias geradas foram:\n{misturas2a2}\n")

# A partir deste nível, devido ao grande número de combinações, os nomes das cores é automático nomeCorSecundária+nomeCorPrimária
print("\nCombinações 3 a 3:\n")
for posSecundaria, corSecundaria in enumerate(misturas2a2):
    for posPrimaria, corPrimaria in enumerate(cores):
        if corPrimaria == corSecundaria[1] or corPrimaria == corSecundaria[2]: continue
        misturas3a3.append([f"{corSecundaria[0]}{corPrimaria}", corSecundaria[1], corSecundaria[2], corPrimaria])
        # input(f"Qual a cor resultante da mistura de {corSecundaria[0]} e {corPrimaria}?")
print(f"\nAs cores terciarias geradas foram:\n{misturas3a3}\n")

print("\nCombinações 4 a 4\n")
for posTerciaria, corTerciaria in enumerate(misturas3a3):
    for posPrimaria, corPrimaria in enumerate(cores):
        if corPrimaria not in [corTerciaria[1:]]:
            misturas4a4.append([f"{corTerciaria[0]}{corPrimaria}", corTerciaria[1], corTerciaria[2], corTerciaria[3], corPrimaria])
            
print(f"\nAs cores auaternárias geradas foram:\n{misturas4a4}\n")
            



