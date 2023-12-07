def calculaSomaProdutosDigitos(num, pesoCont):
    listaPesos = [6,5,4,3,2,9,8,7,6,5,4,3,2]
    if len(num) == 0: return 0    
    
    return (int(num)%10)*listaPesos[pesoCont]+calculaSomaProdutosDigitos(num[:-1],pesoCont-1)

def calculaDigVerificador(somaProdutos):
    if somaProdutos%11<2:
        return 0
    else: 
        return 11-(somaProdutos%11)

def validaCnpj(cnpj):
    digitosInformados = cnpj[-2:]
    cnpj = cnpj[:-2]
    somaProdutos = calculaSomaProdutosDigitos(cnpj, 12)
    dezenaDigVerificador = str(calculaDigVerificador(somaProdutos))
    
    somaProdutos13Digitos = calculaSomaProdutosDigitos(cnpj + str(dezenaDigVerificador), 12)
    
    unidadeDigVerificador = str(calculaDigVerificador(somaProdutos13Digitos))
    
    if dezenaDigVerificador+unidadeDigVerificador == digitosInformados:
        print(f"O CPF {cnpj+digitosInformados} é um CNPJ válido!")
    else: print(f"O CPF {cnpj+digitosInformados} NÃO é um CNPJ válido!")
    
validaCnpj('59541264000103')