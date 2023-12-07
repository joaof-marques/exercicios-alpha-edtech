frase = input("Insira uma frase: ")
tamanhoFrase = len(frase)
vogais = 0
consoantes = 0
espacos = 0
pontuacoes = 0

for caractere in frase:
    if caractere.lower() in "aeiou":
        vogais += 1
    elif caractere.lower() in "bcdfghjklmnpqrstvwxyz":
        consoantes += 1
    elif caractere == " ":
        espacos += 1
    else:
        pontuacoes += 1

print(f"Vogais: {(vogais/tamanhoFrase)*100:.2f}")
print(f"Consoantes: {(consoantes/tamanhoFrase)*100:.2f}")
print(f"Espacos: {(espacos/tamanhoFrase)*100:.2f}")
print(f"Pontuacoes: {(pontuacoes/tamanhoFrase)*100:.2f}")