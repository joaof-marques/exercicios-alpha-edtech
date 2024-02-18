palavra = "Socorram-me subi no ônibus em Marrocos"

def inverte_texto_recursivo(palavra):
    if len(palavra) > 1:
        return palavra[-1]+inverte_texto_recursivo(palavra[:-1])
    return palavra


print(inverte_texto_recursivo(palavra))