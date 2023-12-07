def processar_numeros (num1, num2, callback):
    return callback(num1, num2)

def somaValores (num1, num2):
    return num1+num2

def multiplicaValores (num1, num2):
    return num1*num2

print(processar_numeros(2, 4, somaValores))
print(processar_numeros(2, 4, multiplicaValores))