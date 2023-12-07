def calculadora(num1, num2, *args):
    for operacao in args:
        print(f"{num1}{operacao}{num2} = {eval(f'{num1}{operacao}{num2}')}")
        
        
calculadora(2, 3, '*', '+', '-', '/')