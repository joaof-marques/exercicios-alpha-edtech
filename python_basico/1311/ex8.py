num = int(input("Insira um número para verificar os primos intermediários: "))

cont = 1
qtdeDivisoes = 0
qtdePrimos = 0

while cont < num:
    cont+=1
    #Crivo de Eratóstenes
    #não utilizei OR nos ifs para conseguir contabilizar todas as divisões. Caso usasse o OR eu acabaria contabilizando apenas 1 divisão para todas as comparações (cont%2,3,5,7)
    if cont != 2 and cont%2==0:
        qtdeDivisoes+=1
    elif cont != 3 and cont%3==0:
        qtdeDivisoes+=2
    elif cont != 5 and cont%5==0:
        qtdeDivisoes+=3
    elif cont != 7 and cont%7==0:
        qtdeDivisoes+=4
    else:        
        print(cont)
        qtdePrimos += 1
        qtdeDivisoes += 4
        

print(f"Existem {qtdePrimos} números primos entre 1 e {num}")
print(f"Foram feitas {qtdeDivisoes} divisões para encontrar este resultado")