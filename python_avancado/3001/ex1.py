class Node:
    def __init__(self, valor) -> None:
        self.esquerda = None
        self.direita = None
        self.valor = valor
        
class Arvore:
    def __init__(self, node) -> None:
        self.raiz = node
        
    def inserir_elemento(self, novo_node):
        ponta_insercao = self.raiz
        while True:
            if novo_node.valor == ponta_insercao.valor:
                print("O valor já existe nessa árvore.")
                break
            elif novo_node.valor < ponta_insercao.valor:
                if ponta_insercao.esquerda == None:
                    ponta_insercao.esquerda = novo_node
                    break
                ponta_insercao = ponta_insercao.esquerda
            else: 
                if ponta_insercao.direita == None:
                    ponta_insercao.direita = novo_node
                    break
                ponta_insercao = ponta_insercao.direita
                
    def busca_valor(self, valor):
        ponteiro_varredor = self.raiz
        nivel = 0
        while True:
            if valor == ponteiro_varredor.valor:
                print(f"O valor {valor} está presente na árvore no nível {nivel}!")
                break
            elif valor < ponteiro_varredor.valor:
                if ponteiro_varredor.esquerda == None:
                    print(f"O valor {valor} não está na árvore!")
                    break
                ponteiro_varredor = ponteiro_varredor.esquerda
                nivel += 1
            else:
                if ponteiro_varredor.direita == None:
                    print(f"O valor {valor} não está na árvore!")
                    break
                ponteiro_varredor = ponteiro_varredor.direita
                nivel += 1
        
    def imprimir_em_ordem(self, no_principal):
        if (no_principal.esquerda != None):
            self.imprimir_em_ordem(no_principal.esquerda)
        print(no_principal.valor, end=" ")
        if (no_principal.direita != None):
            self.imprimir_em_ordem(no_principal.direita)
            
    def imprimir_pre_ordem(self, no_principal):
        print(no_principal.valor, end=" ")
        if (no_principal.esquerda != None):
            self.imprimir_pre_ordem(no_principal.esquerda)
        if (no_principal.direita != None):
            self.imprimir_pre_ordem(no_principal.direita)
            
    def imprimir_pos_ordem(self, no_principal):
        if (no_principal.esquerda != None):
            self.imprimir_pos_ordem(no_principal.esquerda)
        if (no_principal.direita != None):
            self.imprimir_pos_ordem(no_principal.direita)
        print(no_principal.valor, end=" ")
        
    def obter_menor_elemento(self, node):
        while node.left:
            node = node.left
        return node.data
            
    def remover_elemento(self, valor, node):    
        if node == None:
            return None
        
        if valor < node.valor:
            node.esquerda = self.remover_elemento(valor, node.esquerda)
        elif valor > node.valor:
            node.direita = self.remover_elemento(valor, node.direita)
        else:
            if node.esquerda == None:
                return node.direita
            elif node.direita == None:
                return node.esquerda
            else:
                substituto = self.obter_menor_elemento(node.direita)
                node.valor = substituto
                node.direita = self.remover_elemento(substituto, node.direita)
                
        return node
            

no_inicial = Node(10)
arvore = Arvore(no_inicial)

arvore.inserir_elemento(Node(5))
arvore.inserir_elemento(Node(15))
arvore.inserir_elemento(Node(3))
arvore.inserir_elemento(Node(9))
arvore.inserir_elemento(Node(12))
arvore.inserir_elemento(Node(17))
arvore.inserir_elemento(Node(1))

# print("\n")
# arvore.busca_valor(1)


# print(f"Árvore pre ordem:")
# arvore.imprimir_pre_ordem(arvore.raiz)

print(f"\n\nÁrvore em ordem:")
arvore.imprimir_em_ordem(arvore.raiz)


# print(f"\n\nÁrvore pos ordem:")
# arvore.imprimir_pos_ordem(arvore.raiz)

arvore.remover_elemento(12, arvore.raiz)

print(f"\n\nÁrvore em ordem:")

arvore.imprimir_em_ordem(arvore.raiz)