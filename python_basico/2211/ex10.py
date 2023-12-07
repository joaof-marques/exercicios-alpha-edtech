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
        "MetaCritic": 90,
        "AntigoDicionario": "Antigo Dicionário"
    },
    "Sekiro: Shadows die twice": {
        "lancamento": 2019,
        "MetaCritic": 90,
        "NovoDicionario": "Novo Dicionario"
    }
}

#Para obter uma lista com todas as chaves podemos utilizar o método keys
chavesJogosSouls = list(jogosSouls.keys())
print(chavesJogosSouls) #['Dark Souls 1', 'Dark Souls 2', 'Dark Souls 3', 'Sekiro: Shadows die twice']
#O mesmo pode ser feito para os valores, utilizando o método value
valoresJogosSouls = list(jogosSouls.values())
print(valoresJogosSouls) #[{'lancamento': 2011, 'MetaCritic': 85}, {'lancamento': 2014, 'MetaCritic': 91}, {'lancamento': 2016, 'MetaCritic': 89}, {'lancamento': 2019, 'MetaCritic': 90, 'NovoDicionario': 'Novo Dicionario'}]