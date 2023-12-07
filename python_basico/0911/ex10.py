tipo = input("Insira o tipo de carne desejada.\n Tipos disponíveis: Filé, Alcatra e Picanha\n").lower()
qtde = float(input("Insira a quantidade de carne desejada: ").replace(",","."))
pagamento = input("Insira o tipo de pagamento: D - Débito, C - Crédito, T - Cartão Tabajara\n").lower()

precoKg = 0

if tipo == "file":
    precoKg = 5.8
elif tipo == "alcatra":
    precoKg = 6.8
elif tipo == "picanha":
    precoKg = 7.8
else:
    print("Opção de carne indisponível")
    exit()

if qtde > 5:
    precoKg -= 0.9
    
descontoPagamento = 0

if pagamento == "t":
    descontoPagamento = 0.05
    
totalCompra = qtde * precoKg
finalComDescontoPagamento = totalCompra * (1-descontoPagamento)


print(f"\nCupom Fiscal:\n{tipo}: {qtde} kgs\t|\tR$ {precoKg:.2f} o kg\t|\tTotal: {qtde*precoKg:.2f} R$\n")

print(f"Valor total da compra: R$ {totalCompra:.2f}\nDesconto extra obtido: R$ {totalCompra - finalComDescontoPagamento:.2f}\nValor final da compra: R$ {finalComDescontoPagamento:.2f}")