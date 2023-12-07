qtdeMorango = float(input("Insira a quantidade (em kg) de morangos: ").replace(",","."))
qtdeMaca = float(input("Insira a quantidade (em kg) de maçãs: ").replace(",","."))

precoMorango = 2.5
precoMaca = 1.8

if qtdeMorango > 5:
    precoMorango = 2.2

if qtdeMaca > 5:
    precoMaca = 1.5
    
totalCompra = qtdeMorango * precoMorango + qtdeMaca * precoMaca

if qtdeMorango+qtdeMaca > 8 or totalCompra > 25:
    finalComDescontoExtra = totalCompra * 0.9
    descontoExtraObtido = totalCompra - finalComDescontoExtra

print(f"Relatório da Compra:\nMorango: {qtdeMorango} kgs\t|\tR$ {precoMorango} o kg\t|\tTotal: {qtdeMorango*precoMorango} R$\nMaca:    {qtdeMaca} kgs\t|\tR$ {precoMaca} o kg\t|\tTotal: {qtdeMaca*precoMaca} R$\n")

print(f"Valor total da compra: R$ {totalCompra:.2f}\nDesconto extra obtido: R${descontoExtraObtido:.2f}\nValor final da compra: R${finalComDescontoExtra:.2f}")
    