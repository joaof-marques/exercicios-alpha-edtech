string = input("Insira a string a ser formatada: ")

def aplica_funcao_arbitraria(funcao, string):
    return funcao(string)


def tudo_maiusculo(string):
    stringMaiuscula = ""
    for letra in string:
        stringMaiuscula += letra.upper()
        
    return stringMaiuscula

def alterna_maiusculo_minusculo(string):
    stringFinal = ""
    
    for pos, caractere in enumerate(string):
        if pos%2==0:
            stringFinal += caractere.upper()
        else:
            stringFinal += caractere.lower()
            
    return stringFinal

print(aplica_funcao_arbitraria(tudo_maiusculo, string))
print(aplica_funcao_arbitraria(alterna_maiusculo_minusculo, string))