q1 = input("Telefonou para a vítima? ").lower()
q2 = input("Esteve no local do crime? ").lower()
q3 = input("Mora perto da vítima? ").lower()
q4 = input("Devia para a vítima? ").lower()
q5 = input("Já trabalhou com a vítima? ").lower()

contador = 0

if q1 == "sim":
    contador+=1
    
if q2 == "sim":
    contador+=1
    
if q3 == "sim":
    contador+=1
    
if q4 == "sim":
    contador+=1
    
if q5 == "sim":
    contador+=1

if contador == 2:
    print("Suspeita")
elif contador == 3 or contador == 4:
    print("Cúmplice")
elif contador == 5:
    print("Assassino")
else: print("Inocente")