num = int(input("Insira o número para verificar se é ou não um fatorial: "))

resFatorial = 1
cont = 1
while True:
    #calcula fatorial
    resFatorial *= cont
    
    if resFatorial == num:
        print(f"O número {num} é o fatorial de {cont}.")
        break 
    elif resFatorial > num:
        print(f"O número {num} não é um fatorial.")
        break
    
    cont+=1
      