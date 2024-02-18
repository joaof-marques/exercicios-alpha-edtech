def calcular_emissoes(usinas, indice=0):
    
    if indice > len(usinas)-1:
        return 0
    
    return usinas[indice][1]*usinas[indice][2] + calcular_emissoes(usinas, indice+1)

usinas = [
    ("Solar", 120, 0),
    ("Eólica", 200, 0),
    ("Fóssil", 500, 0.7)
]

print(calcular_emissoes(usinas))