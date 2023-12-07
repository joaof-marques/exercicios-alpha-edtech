cont = 0
danoRyu = 0
danoKen = 0
roundsRyu = 0
roundsKen = 0

while True:
    golpe = int(input(f"Insira o valor do golpe {cont+1}: "))
    if golpe > 0:
        danoRyu += golpe
    elif golpe < 0:
        danoKen -= golpe
    else:
        if danoRyu > danoKen:
            roundsRyu += 1
            print("Ponto Ryu")
        elif danoRyu < danoKen:
            roundsKen += 1
            print("Ponto Ken")
        elif danoRyu != 0:
            roundsRyu += 1
            roundsKen += 1
            print("Round empatado!")
        
        break
    
    print(f"danoRyu: {danoRyu}, danoKen: {danoKen}")
    
    if danoRyu >= 100:
        roundsRyu += 1
        print("Ponto Ryu")        
        danoRyu, danoKen = 0, 0
    elif danoKen >=100:
        roundsKen += 1
        danoRyu, danoKen = 0, 0
        print("Ponto Ken")
    cont+=1
    
if roundsRyu > roundsKen:
    print("Ryu vence!")
elif roundsRyu < roundsKen:
    print("Ken vence!")
else: print("Empate.")