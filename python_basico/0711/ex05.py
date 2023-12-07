nome = input("Insira o nome do vendedor: ")
salarioFixo = float(input("Insira o salário fixo deste vendedor: "))
totalVendas = int(input("Insira o valor das vendas realizadas por este vendedor: "))

salarioFinal = salarioFixo + (totalVendas*0.05)

print(f"O salário final do vendedor {nome} é R${salarioFinal:.2f}")