def executar_operacao (num, callback):
    return callback(num)

def dobro (num):
    return 2*num

def inverso (num):
    return 1/num

print(executar_operacao(4, dobro))
print(executar_operacao(4, inverso))