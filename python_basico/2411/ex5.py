from fibonacci import fibonacci
# Para instalar módulos/pacotes externos, utilizamos o comando pip install nomeDoPacote
# Nesse exemplo estou usando o pacote py-fibonacci 

# % pip install py-fibonacci
# Defaulting to user installation because normal site-packages is not writeable
# Collecting py-fibonacci
#   Downloading py_fibonacci-0.5.2-py3-none-any.whl (3.6 kB)
# Installing collected packages: py-fibonacci
# Successfully installed py-fibonacci-0.5.2

# Após instalar o pacote no meu computador, posso incluí-lo como um módulo e utilizá-lo normalmente

# A função fibonacci da biblioteca py-fibonacci retorna uma list com a sequência indo até o valor informado
print(fibonacci(40))
print(fibonacci(56))