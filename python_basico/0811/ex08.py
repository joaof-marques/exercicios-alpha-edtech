file = open("foo.txt", "w")
file.write("Esse é o novo conteúdo do arquivo e nenhum problema com conteúdo antigo vai ocorrer pois todo ele já foi apagado antes da gravação desta string")
file.close()

file = open("foo.txt", "r")
print(file.read())
file.close()