qtdeEleitores = int(input("Insira a quantidade de eleitores: "))
cand1 = 0
cand2 = 0
cand3 = 0

for i in range (qtdeEleitores):
    voto = int(input("Favor inserir o voto: "))
    if voto == 1: cand1 += 1
    elif voto == 2: cand2 += 1
    elif voto == 3: cand3 += 1
    else: print("Candidato inválido. O voto será anulado")


print(f"Pontuação final:\nCandidato 01: {cand1} votos\nCandidato 02: {cand2} votos\nCandidato 03: {cand3} votos")