import os
estoque_armazens = []
opcao=0
while opcao != 4:
    opcao = int(input("Insira a opção desejada:\n1 - Criar armazém e cadastrar produtos\n2 - Consultar armazém e produtos cadastrados\n3 - Inserir/Remover itens de um armazém\n4 - Encerrar execução do programa\n\n"))
    os.system('clear')
    if opcao == 1:
        print(f"Armazém {len(estoque_armazens)+1} criado!")
        qtdeItems = int(input("Favor inserir quantos itens serão cadastrados no armazém: "))
        items = []
        for i in range(qtdeItems):
            items.append(input(f"Favor inserir o nome do item {i+1}: "))
        estoque_armazens.append(frozenset(items))
        
        os.system('clear')
        print(f"Itens cadastrados com sucesso no Armazém {len(estoque_armazens)}\n")         
    elif opcao == 2:
        if len(estoque_armazens)==0:
            os.system('clear')
            print("Nenhum armazém foi cadastrado, favor cadastrar antes de realizar a consulta.\n")
        else:
            armazem = int(input(f"De qual armazém deseja consultar o estoque?\nAtualmente os seguintes armazéns estão cadastrados: 1 até {len(estoque_armazens)}: \n"))
            os.system('clear')
            print(f"\nEstoque cadastrado no Armazém {armazem}:\n")
            for i in estoque_armazens[armazem-1]:
                print(f"Item em estoque: {i}")
            print('\n')            
    elif opcao == 3:
        while True:
            armazem = int(input("Insira o armazém no qual o item será adicionado/removido: \n"))
            os.system('clear')                
            if armazem <= 0 or armazem > len(estoque_armazens):
                print("Opção inválida. Tente novamente\n")
            else: break
        lista_estoque_armazem = set(estoque_armazens[armazem-1])
        
        while True:
            os.system('clear')
            opcaoAdicionarRemover = int(input("Insira a opção desejada:\n1 - Adicionar item\n2 - Remover item\n3 - Voltar ao menu inicial\n"))
            if opcaoAdicionarRemover not in [1, 2, 3]:
                print("Opção inválida. Tente novamente\n")
            else: break
        
        if opcaoAdicionarRemover == 1:
            os.system('clear')
            lista_estoque_armazem.add(input("Insira o item a ser adicionado: "))
            estoque_armazens[armazem-1] = frozenset(lista_estoque_armazem)
            print("Item adicionado com sucesso!\n")
            
        elif opcaoAdicionarRemover == 2:
            os.system('clear')
            lista_estoque_armazem.remove(input("Insira o item a ser removido: "))            
            estoque_armazens[armazem-1] = frozenset(lista_estoque_armazem)
            print("Item removido com sucesso!\n")   
                     
        elif opcaoAdicionarRemover == 3:
            continue    
        
    elif opcao == 4:
        print("Obrigado por utilizar nosso sistema.")
        break
    
    else: 
        os.system('clear')        
        print("Opção inválida. Favor informar uma opção válida.\n")