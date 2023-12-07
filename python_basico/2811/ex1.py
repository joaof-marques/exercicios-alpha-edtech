def calcularMedia (*args):
    soma = 0
    for num in args:
        soma += num
    
    return soma/len(args)

print(calcularMedia(3, 5, 7, 9))
print(calcularMedia(5,9))
