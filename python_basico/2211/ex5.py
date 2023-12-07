jogosSouls = {
    "Dark Souls 1": {
        "lancamento": 2011,
        "MetaCritic": 85
    },
    "Dark Souls 2": {
        "lancamento": 2014,
        "MetaCritic": 91
    },
    "Dark Souls 3": {
        "lancamento": 2016,
        "MetaCritic": 89
    },
    "Sekiro: Shadows die twice": {
        "lancamento": 2019,
        "MetaCritic": 90
    }
}

#É possível sim, e por coincidência o exemplo que eu criei desde o início já utilizava esse conceito.
#É importante os valores de cada chave pode ser de qualquer tipo. Você pode ter uma chave com seu respectivo valor sendo string, int, float, bool, obj, list, tuple, etc
#Porém, as chaves em si só podem receber elementos imutáveis, então não é possível declarar uma chave do tipo lista
#Para acessar o ano de lançamento de Dark Souls 2, por exemplo, fazemos o seguinte:
# print(jogosSouls["Dark Souls 1"]["lancamento"])
#Para compreender, vamos quebrar jogosSouls["Dark Souls 1"]["lancamento"] em 2 partes:
#jogosSouls["Dark Souls 1"] se refere à chave "Dark Souls 1" do dicionário jogosSouls. Então toda essa primeira parte tornou-se dicionário relativo ao primeiro jogo
#Para facilitar a compreensão, podemos fazer o seguinte:
darkSouls1 = jogosSouls["Dark Souls 1"]
# print(darkSouls1) #Saída esperada: {'lancamento': 2011, 'MetaCritic': 85}
#Agora que já temos o objeto, precisamos acessar a chave lancamento inicialmente desejada acrecestando o nome da chave:
#print(jogosSouls["Dark Souls 1"]["lancamento"]) ou print(darkSouls1["lancamento"])
print(jogosSouls["Dark Souls 1"]["lancamento"])
print(darkSouls1["lancamento"])
#Ambos os casos vão imprimir 2011
