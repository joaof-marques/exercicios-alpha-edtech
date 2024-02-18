try:
    with open("/etc/vdpau_wrapper.cfg","w") as arquivo: #arquivo com permissões necessárias
        print(arquivo.write("asdf"))
except FileNotFoundError:
    print("Arquivo não encontrado. Tente ajustar o nome do arquivo")
except PermissionError:
    print("Você não tem permissão para acessar/modificar o arquivo.")