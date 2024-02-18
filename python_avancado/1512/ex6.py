import math

def converte_para_int (num:float) -> None:
    valor_inteiro = math.floor(num)
    print(valor_inteiro**2)
    
try:
    entrada = float(input("Insira um valor: ").replace(",", "."))
    converte_para_int(entrada)
except ValueError:
    print("Entrada inválida")

