def saudaAluno (nomeAluno):
    print(f"Olá {nomeAluno}!\nBem vindo(a) ao curso de Python!")
    
def imprimeDadosAluno(nome, idade:18, endereco, cep):
    saudaAluno(nome.split(" ")[0])
    print(f"Nome Completo: {nome}")
    print(f"Idade: {idade}")
    print(f"Endereço: {endereco}")
    print(f"CEP: {cep}")
    
def recebeDadosAluno():
    nome = input("Insira o nome completo do Aluno: ")
    idade = int(input("Insira a idade do aluno: "))
    endereco = input("Insira o endereço do aluno: ")
    cep = input("Insira o CEP do aluno: ")
    
    imprimeDadosAluno(nome, idade, endereco, cep)

recebeDadosAluno()
    