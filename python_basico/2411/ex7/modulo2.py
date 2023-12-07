import modulo1

def vingadores ():
    homemFerro = modulo1.superHeroi("Homem de Ferro", "Avengers")
    homemAranha = modulo1.superHeroi("Homem Aranha", "Avengers")
    hulk = modulo1.superHeroi("hulk", "Avengers")
    
    return [homemFerro, homemAranha, hulk]

def ligaJustica ():
    batman = modulo1.superHeroi("Batman", "Liga da Justiça")
    superHomem = modulo1.superHeroi("Super Homem", "Liga da Justiça")
    marciano = modulo1.superHeroi("Marciano", "Liga da Justiça")
    
    return [batman, superHomem, marciano]
    