cont = 0

while cont < 3:
    cont+=1
    usuario = input("Favor inserir o usuário: ")
    senha = input("Favor inserir a senha: ")
    
    if usuario == senha:
        print("O campo senha não pode ser igual ao campo usuário")
             
    else:
        print("Usuário logado com sucesso!")
        break
    
    if cont==3:
        print("Quantidade limite de tentativas excedida. Tente novamente mais tarde.")