import biblioteca
import importlib

print(biblioteca.livros)
biblioteca.imprimirCatalogo()
biblioteca.livros = "Harry Potter"
print(biblioteca.livros)
importlib.reload(biblioteca)
biblioteca.imprimirCatalogo()


#No exemplo acima, fizemos uma modificação em livros mas era necessário voltar ao estado inicial
#Então executamos o importlib.reload(biblioteca) para recarregar a biblioteca e restaurar os valores para os default

#Saída sem o reload:
# Vazio
# Vazio
# Harry Potter
# Harry Potter

#Saída com o reload:
# Vazio
# Vazio
# Harry Potter
# Vazio