def divide_1(entrada:int) -> None:
    try:
        print(1/entrada)
    except ZeroDivisionError:
        print("Divisão por zero não é definida. Tente novamente")
    finally:
        print("João Pedro Marques")
        
def recebe_entrada_usuario():
    entrada = input("insira um número: ").replace(",", ".")
    try:
        entrada = float(entrada)
    except ValueError:
        print("A entrada precisa ser do tipo numérico")
        exit()
    return entrada
    
entrada = recebe_entrada_usuario()
divide_1(entrada)