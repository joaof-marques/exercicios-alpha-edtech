from minhaMath import calculaFatorial

def somatorioInversoFatorial (num):
    somatorio = 0
    for i in range(1, num+1):
        somatorio += 1/calculaFatorial(i)
        print(f"i: {i}, fatorial: {calculaFatorial(i)}, Somatorio: {somatorio}")
        
    return somatorio

print(somatorioInversoFatorial(20))