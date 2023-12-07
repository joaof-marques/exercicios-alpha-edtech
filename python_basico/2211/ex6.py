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

#Existem duas maneiras de remover uma chave de um dicionário: del e pop
#Utilizamos o del da seguinte maneira:
# del jogosSouls["Dark Souls 3"]
# print(jogosSouls) #Saída esperada: {'Dark Souls 1': {'lancamento': 2011, 'MetaCritic': 85}, 'Dark Souls 2': {'lancamento': 2014, 'MetaCritic': 91}, 'Sekiro: Shadows die twice': {'lancamento': 2019, 'MetaCritic': 90}}
#Conforme verificado, a palavra del remove a chave informada (pode ser usada para qualquer coisa em python: variávels, listas, tuplas, etc)
#Porém, caso não exista a chave informada, o del joga um erro na execução. E para resolver isso, podemos usar o método pop
sekiro = jogosSouls.pop("Sekiro: Shadows die twice", None)
print(jogosSouls) #{'Dark Souls 1': {'lancamento': 2011, 'MetaCritic': 85}, 'Dark Souls 2': {'lancamento': 2014, 'MetaCritic': 91}, 'Dark Souls 3': {'lancamento': 2016, 'MetaCritic': 89}}
print(sekiro) #{'lancamento': 2019, 'MetaCritic': 90}
#Note que o jogo Sekiro foi removido do dicionário jogosSouls e foi atribuído à variável sekiro.
#uma outra diferença é o segundo argumento do método pop. Podemos informar qual vai ser o valor retornado caso o primeiro argumento (ou seja, a chave) não seja encontrada no dicionário
#Isso evita que existam erros na execução e ainda nos possibilita padronizar os dados e tratar todas as situações