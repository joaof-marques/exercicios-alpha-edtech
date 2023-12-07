def gerarNumPrimo (qtde):
    numerosGerados = []
    num = 2
    while len(numerosGerados)<qtde:
        if 0 not in (num%2, num%3, num%5, num%7) or num in (2, 3, 5, 7):
            numerosGerados.append(num)
        num+=1
    
    return numerosGerados