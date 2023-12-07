num1 = 0
num2 = 1
aux = 0

print(num1)
for i in range(1, 30):
    aux = num2
    num2 += num1
    num1 = aux
    print(num1)
    
    if num1 >= 500:
        exit()