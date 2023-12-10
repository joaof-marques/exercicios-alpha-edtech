
def validaTamanhoCpf(cpf):
    
    if isinstance(cpf, int):
        return "Tamanho Correto!" if len(str(cpf))==11 else "Tamanho errado!"
    elif isinstance(cpf, str):
        return "Tamanho Correto!" if len(cpf)==11 else "Tamanho errado!"
    elif isinstance(cpf, list):
        cpfString = "".join(cpf)
        return "Tamanho Correto!" if len(cpf)==11 else "Tamanho errado!"
    else:
        return "Tipo de dado não suportado"

resultado_1 = validaTamanhoCpf(1234567890)
resultado_2 = validaTamanhoCpf("12345678910")
resultado_3 = validaTamanhoCpf(["1", "2", "3", "4", "5", "6", "7", "8", "9", "1", "2"])

 
print(resultado_1)
print(resultado_2)
print(resultado_3)