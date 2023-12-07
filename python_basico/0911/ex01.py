data = input("Insira uma data no formato dd/mm/aaaa: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])
bissexto = False

if ano%4==0:
    bissexto = True
    if ano%100==0 and not ano%400==0:
        bissexto = False
        
# if mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12:
if (mes<=7 and mes%2==1) or (mes>=8 and mes%2==0):
    if dia>00 and dia<=31:
        print("Data Valida")
    else: print("Data Invalida")
elif mes==4 or mes==6 or mes==9 or mes==11:
    if dia>00 and dia<=30:
        print("Data Valida")
    else: print("Data Invalida")
elif mes==2:
    if bissexto:
        if dia>00 and dia<=29:
            print("Data Valida")
        else: print("Data Invalida")
    else:
        if dia>00 and dia<=28:
            print("Data Valida")
        else: print("Data Invalida")