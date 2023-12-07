qtdeDados = int(input("Informe a quantidade de dados a serem inseridos: "))
dados = []


for i in range(qtdeDados):
    dados.append(int(input(f"Insira o valor {i+1}: ")))

with open("arrayEx1.txt", "w") as arquivo:
    arquivo.write(str(dados))
    