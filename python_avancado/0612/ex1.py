alunos = []

def saudaAluno (nomeAluno):
    print(f"Olá {nomeAluno}!\nBem vindo(a) ao curso de Python!")
    
def imprimeDadosAluno(nome, idade:18, endereco, cep):
    saudaAluno(nome.split(" ")[0])
    
    
def recebeDadosAluno():
    nome = input("Insira o nome completo do Aluno: ")
    idade = int(input("Insira a idade do aluno: "))
    endereco = input("Insira o endereço do aluno: ")
    cep = input("Insira o CEP do aluno: ")
    cadastraAluno(nome, idade, endereco, cep)
    imprimeDadosAluno(nome, idade, endereco, cep)

def cadastraAluno (nome, idade, endereco, cep):
    
    aluno = {"nome": nome, "idade": idade, "endereco": endereco, "cep": cep, "matricula": 9000+len(alunos)+1}
    
    alunos.append(aluno)
    
def listarAlunos ():
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} - Matrícula: {aluno['matricula']}")

while True :
    opcao = int(input("Insira a opcao desejada:\n1 - Cadastrar Aluno\n2 - Listar Alunos\n3 - Sair\n"))
    if opcao == 3:
        break
    elif opcao == 1:
        recebeDadosAluno()
    elif opcao == 2:
        listarAlunos()
    else: print("Opção Inválida")
    