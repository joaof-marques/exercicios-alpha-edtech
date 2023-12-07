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

#Para adicionar uma nova chave-valor ao dicionário, basta apenas atribuir um valor à ela. Mesmo ainda não existindo, o Python interpretará isso como a criação da informação e guardará o que for necessário
jogosSouls["BloodBorne"] = {"lancamento": 2015, "MetaCritic": 92}
print(jogosSouls) #Saída esperada: {'Dark Souls 1': {'lancamento': 2011, 'MetaCritic': 85}, 'Dark Souls 2': {'lancamento': 2014, 'MetaCritic': 91}, 'Dark Souls 3': {'lancamento': 2016, 'MetaCritic': 89}, 'Sekiro: Shadows die twice': {'lancamento': 2019, 'MetaCritic': 90, 'NovoDicionario': 'Novo Dicionario'}, 'BloodBorne': {'lancamento': 2015, 'MetaCritic': 92}}
#É possível verificar ao final do dicionário o objeto BloodBorne