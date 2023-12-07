num = int(input("Insira um número para verificar se é primo: "))

cont = 1
divisores = 0

while cont < num:
    if num%cont==0:
        divisores += 1
    cont+=1
        
if divisores <= 1:
    print(f"O número {num} é primo!")
else:
    print(f"O número {num} não é primo.")