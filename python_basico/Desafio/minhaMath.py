def calculaFatorial (num):
    cont = 1
    if num == 0: return 1
    fatorial = 1
    while cont <= num:
        fatorial *= cont
        cont+=1
    
    return fatorial