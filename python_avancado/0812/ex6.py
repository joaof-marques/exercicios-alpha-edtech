from typing import List
import os

biblioteca = []

def recebe_livro() -> dict:
    os.system("clear")
    titulo = input("Insira o título do livro: ")
    autor = input("Insira o autor do livro: ")
    ano = input("Insira o ano do livro: ")
    
    
    return {"titulo": titulo, "autor": autor_abnt(autor), "ano": int(ano)}

def cadastrar_livro(livro):
    biblioteca.append(livro)
    print("Livro cadastrado com sucesso!")

def listar_livros_cadastrados (biblioteca):
    for livro in biblioteca:
        print(f"Livro: {livro['titulo']} \t|\tAutor: {livro['autor']} \t|\tAno: {livro['ano']}")
        
def autor_abnt(nome):
    nomeAbnt = nome[nome.rfind(' ')+1:] + ", "
    cursor = 0
    while nome.rfind(" ") != -1:
        nomeAbnt += nome[cursor] + ", "
        nome = nome[nome.find(" ")+1:]
        
    return nomeAbnt[:-2]

while True:
    opcao = int(input("Insira a opção desejada: \n1 - Cadastrar livro\n2 - Listar livros cadastrados\n0 - Encerrar programa\n"))
    
    if opcao == 0:
        break
    elif opcao == 1:
        livro = recebe_livro()
        cadastrar_livro(livro)
    elif opcao == 2:
        listar_livros_cadastrados(biblioteca)
        
    
