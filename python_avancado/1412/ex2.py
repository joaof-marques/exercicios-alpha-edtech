frases = ["Suponha que você tenha uma lista de strings representando frases", "Crie uma função em Python que recebe essa lista e duas funções de ordem superior como argumentos", "A primeira função deve ser responsável por tokenizar cada frase em palavras, enquanto a segunda função deve processar essas palavras de acordo com algum critério (por exemplo, converter todas as letras para maiúsculas)"]

def tokeniza_frases (frases):
    frases_tokenizado = []
    for i in frases:
        frases_tokenizado.append(i.split(" "))
    return frases_tokenizado

#Faz uma palavra maiuscula, uma minuscula
def altera_caracteres(frases):
    for frase in frases:
        for pos, palavra in enumerate(frase):
            if pos%2==0:
                frase[pos] = palavra.upper()
    return frases

def aplica_funcoes_secundarias(frases, funcao1, funcao2):
    resultado1 = funcao1(frases)
    resultado2 = funcao2(resultado1)
    return resultado2

resultado = aplica_funcoes_secundarias(frases, tokeniza_frases, altera_caracteres)
print(resultado)