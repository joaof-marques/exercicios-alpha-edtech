cores = ['amarelo', 'azul']
misturas = []

print("\nCombinações 2 a 2:\n")
for posCor1, cor1 in enumerate(cores):
    for posCor2, cor2 in enumerate(cores):
        if posCor2 <= posCor1: continue
        misturas.append(input(f"Qual a cor resultante da mistura {cor1} e {cor2}? "))

misturas.append(input(f"Qual a cor resultante da mistura amarelo, azul e vermelho? "))
print(misturas)