file = open("foo.txt", "r")

numInteiro = int(file.readline().strip())
numFloat = file.readline().strip()
numFloat = float(numFloat.replace(",", "."))
nome = file.readline().strip()

print(numInteiro * 2, numFloat, nome)