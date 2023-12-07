qtdeLitros = float(input("Insira a quantidade de combustível desejada: ").replace(",", "."))
tipo = input("Insira o tipo de combustível desejado: A para Álcool e G para Gasolina. ").lower()

if tipo=="a":
    combustivel = "Álcool"
    desconto = 0.03
    if qtdeLitros>20:
        desconto=0.05
    precoFinal = qtdeLitros*1.9*(1-desconto)
elif tipo == "g":
    combustivel = "Gasolina"
    
    desconto = 0.04
    if qtdeLitros>20:
        print("entrou")
        desconto=0.06
        print(f"Desconto: {desconto}\n")    
        
    print(f"Desconto: {desconto}\n")    
    precoFinal = qtdeLitros*2.5*(1-desconto)
    
print(f"Para a quantidade de {qtdeLitros} litros de {combustivel}, o desconto é {desconto*100}% por litro, totalizando R$ {precoFinal} para pagamento")