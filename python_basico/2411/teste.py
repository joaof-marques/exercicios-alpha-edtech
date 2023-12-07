a = 10

def minha_funcao(adicionar, multiplicar):
    global a
    a = a * multiplicar + adicionar
    print(a)

minha_funcao(4, 2)
print(a)    