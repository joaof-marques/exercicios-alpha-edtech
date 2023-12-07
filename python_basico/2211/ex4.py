jogosSouls = {
    "Dark Souls 1": {
        "lançamento": 2011,
        "MetaCritic": 85
    },
    "Dark Souls 2": {
        "lançamento": 2014,
        "MetaCritic": 91
    },
    "Dark Souls 3": {
        "lançamento": 2016,
        "MetaCritic": 89
    },
    "Sekiro: Shadows die twice": {
        "lançamento": 2019,
        "MetaCritic": 90
    }
}

#Podemos iterar um objeto usando um loop convencional:
# for chave in jogosSouls:
#     print(chave)
#Caso não seja claramente modificado, a iteração padrão ocorre pelas chaves, porém, é possível acessar os valores utilizando nomeDoDicionario[nomeDaChave]
# for chave in jogosSouls:
#     print(jogosSouls[chave])
#O primeiro exemplo imprimirá todas as chaves do objeto jogosSouls (Dark Souls 1, Dark Souls 2, Dark Souls 3, Sekiro: Shadows die twice)
#Já o segundo exemplo imprimirá os valores ligados à essas chaves (lançamento e MetaCritic)
