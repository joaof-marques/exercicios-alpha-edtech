numero = int(input("Insira um número inteiro de 4 dígitos: "))

unidade = numero%10
numero -= unidade
dezena = (numero%100)//10
numero -= dezena*10
centena = (numero%1000//100)
numero -= centena
milhar = (numero&10000)//1000



unidade = (unidade+1)%10
dezena = (dezena+1)%10
centena = (centena+1)%10
milhar = (milhar+1)%10

print(f"{milhar}{centena}{dezena}{unidade}")
