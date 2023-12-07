a, b = 0, 1
fibNum = 0

while a <= 500:
    aux = a + b
    a = b
    b = aux
    print(a)