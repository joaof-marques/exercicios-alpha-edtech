def converteTemperatura(temp, opcao):
    if opcao == '1':
        temp = (temp * 9/5) + 32
        return f"{temp}° Fahrenheit"
    else:
        temp = (temp - 32) * 5/9
        return f"{temp}° Celsius"
        
    

opcao = input("Selecione uma opção:\n1 - Converter de Celsius para Fahrenheit\n2 - Converter de Fahrenheit para Celsius \n")
temp = int(input("Insira a temperatura para a conversão: "))

print(converteTemperatura(temp, opcao))