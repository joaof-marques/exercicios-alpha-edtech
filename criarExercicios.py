import sys
import os

pasta_alvo= sys.argv[1]
for i in range(1, 11):
    caminho_arquivo = os.path.join(pasta_alvo, f"ex{i}.py")
    with open(caminho_arquivo, "w") as arquivo:
        pass
    
