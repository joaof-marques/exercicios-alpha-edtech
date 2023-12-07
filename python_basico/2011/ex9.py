import os
estoque_armazens = []
opcao=0
while opcao != 3:
    opcao = int(input("Insira a opção desejada:\n1 - Criar armazém e cadastrar produtos(depois de cadastrados, os produtos não poderão ser alterados)\n2 - Consultar armazém e produtos cadastrados\n3 - Encerrar execução do programa\n\n - - - Para ambas as opções será necessário informar o armazém desejado - - -\n"))
    
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
            print(f"\nEstoque cadastrado no Armazém {armazem}:\n")
            for i in estoque_armazens[armazem-1]:
                print(f"Item em estoque: {i}")
            print('\n')
    elif opcao == 3:
        print("Obrigado por utilizar nosso sistema.")
        break
    
    else: 
        os.system('clear')        
        print("Opção inválida. Favor informar uma opção válida.\n")