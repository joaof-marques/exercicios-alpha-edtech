#Informações retiradas de https://homepages.dcc.ufmg.br/~rodolfo/aedsi-2-10/regrasDigitosVerificadoresCPF.html

def calculaSomaProdutosDigitos(num, peso):
    if len(num) == 0: return 0
    # ancora = 11
    # if len(num) == 10:
    #     ancora = 12
    # peso = ancora-(len(num))   || 11-(len(num))+len(num)%9
    return (int(num)%10)*peso+calculaSomaProdutosDigitos(num[:-1],peso+1)

def calculaDigVerificador(somaProdutos):
    if somaProdutos%11==0 or somaProdutos%11==1:
        return 0
    else: 
        return 11-(somaProdutos%11)
    

def validaCpf(cpf):
    digitosInformados = cpf[-2:]
    cpf = cpf[:-2]
    somaProdutos = calculaSomaProdutosDigitos(cpf, 2)
    
    dezenaDigVerificador = str(calculaDigVerificador(somaProdutos))
    
    somaProdutos10Digitos = calculaSomaProdutosDigitos(cpf + str(dezenaDigVerificador), 2)
    
    unidadeDigVerificador = str(calculaDigVerificador(somaProdutos10Digitos))
    
    if dezenaDigVerificador+unidadeDigVerificador == digitosInformados:
        print(f"O CPF {cpf+digitosInformados} é um CPF válido!")
    else: print(f"O CPF {cpf+digitosInformados} NÃO é um CPF válido!")
    
    
validaCpf('12345678912')
