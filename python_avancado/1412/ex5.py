def divide_entradas_usuario () -> float:
    entrada1:float = float(input("Insira o primeiro valor: "))
    entrada2:float = float(input("Insira o segundo valor: "))
    
    try:
        resultado:float = entrada1/entrada2
    except ZeroDivisionError:
        print("Divisão por zero não é definida. Tente novamente")
        return
        
    return resultado

print(divide_entradas_usuario())