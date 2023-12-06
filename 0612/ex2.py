numeros = []

def cadastraNumeros (num):
    numeros.append(num)
    
def somatorioNumeros (numeros):
    soma = 0
    for num in numeros:
        soma += num
    print(f"Somatório sem modificar a lista: {soma}")
    
cont = int(input("Insira quantos números quer cadastrar: "))

print(f"Lista original: {numeros}")
for i in range(cont):
    cadastraNumeros(int(input(f"Insira o {i+1}° número: ")))

print(f"Lista modificada: {numeros}")
somatorioNumeros(numeros)
print(f"Lista após somatório sem alteração: {numeros}")
