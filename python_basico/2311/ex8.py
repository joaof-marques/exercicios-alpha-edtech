num1 = 0
num2 = 1
n = int(input("Insira a quantidade de números Fibonacci desejados: "))

def calculaFibo (num1, num2, n):
    if n == 0:
        print("\n")
        return 0
    print(num1, end=", ")
    num1, num2 = num2, num1+num2
    return calculaFibo(num1, num2, n-1)

calculaFibo(num1, num2, n)