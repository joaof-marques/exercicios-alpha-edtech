def calculaSomaDigitos(num):
    if num == 0:
        return 0
    return num%10+calculaSomaDigitos(num//10)

print(calculaSomaDigitos(112))
print(calculaSomaDigitos(123456789))
print(calculaSomaDigitos(987654321))