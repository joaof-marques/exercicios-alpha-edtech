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

#Não é possível ter duas chaves com o mesmo nome em um dicionário
#Apesar de ser possível declarar ou inserir chaves que já existam (e por possível eu digo não gerar um erro), isso não significa que podem existir duas chaves com o mesmo nome.
#O que acontece é que a segunda chave de mesmo nome, ou a segunda inserção, vai sobrescrever a primeira e as informações da primeira serão totalmente perdidas.
print(jogosSouls["Sekiro: Shadows die twice"]) #saída esperada: {'lancamento': 2019, 'MetaCritic': 90, 'Novo': 'novo'}
#Acredito que siga o mesmo raciocínio de fazermos variavelA = 10 e na linha seguinte fazermos variavelA = 20. O que ocorre é que a segunda atribuição apaga a primeira ocorrencia.