numeroBase = int(input("Insira um número para filtrarmos as impressões: "))

for i in range(1,50):
    if i%numeroBase==0:
        print(i)
