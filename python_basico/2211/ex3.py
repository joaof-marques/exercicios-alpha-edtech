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
#Podemos utilizar o operador in para verificar se uma chave está presente no dicionário
#print("Dark Souls 3" in jogosSouls) #Saída esperada: True, pois "Dark Souls 3" é um jogo já lançado e existente no dicionário
#print("Dark Souls 4" in jogosSouls) #Saída esperada: False, pois "Dark Souls 4" não é um jogo lançado e não existente no dicionário

#Podemos utilizar também o método get
#Esse método retorna o valor da chave informada.
#print(jogosSouls.get("Sekiro: Shadows die twice")) #Saída esperada: {'lançamento': 2019, 'MetaCritic': 90}
#Caso a string (chave) informada como parâmetro para o get não exista, o valor retornado será None
#print(jogosSouls.get("BloodBorne")) #Saída esperada: None


#Podemos também tentar utilizar um outro conceito chamado Thruthiness. Esse conceito trata da possibilidade de interpretar valores não boleanos como True ou False.
#Uma lista vazia [], é sinônimo de False, enquanto que uma lista com pelo menos um item ["A"], é interpretado como verdadeiro.
#if jogosSouls["Dark Souls 3"]: print(jogosSouls["Dark Souls 3"])
#Porém, no Python, diferente de outras linguagens, como JS, quando não existe a chave passada como parâmetro, o programa para a execução.
#Então essa lógica funciona para valores existentes, mas é necessário tratar a não existência dos valores com um try except.
#É mais uma alternativa para a verificação da existência de alguma chave (porém, o uso do IN ainda é o mais recomendado)
