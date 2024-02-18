comentarios = [
    {"likes": 65, "dislikes": 20, "amei": 78},
    {"likes": 48, "dislikes": 15, "amei": 92},
    {"likes": 32, "dislikes": 8, "amei": 50},
    {"likes": 75, "dislikes": 30, "amei": 61},
    {"likes": 90, "dislikes": 25, "amei": 84},
    {"likes": 40, "dislikes": 12, "amei": 73},
    {"likes": 56, "dislikes": 18, "amei": 65},
    {"likes": 70, "dislikes": 22, "amei": 89},
    {"likes": 43, "dislikes": 15, "amei": 75},
    {"likes": 68, "dislikes": 28, "amei": 91},
    {"likes": 55, "dislikes": 10, "amei": 42},
    {"likes": 80, "dislikes": 35, "amei": 70},
    {"likes": 36, "dislikes": 14, "amei": 60},
    {"likes": 58, "dislikes": 26, "amei": 88},
    {"likes": 77, "dislikes": 19, "amei": 82},
    {"likes": 52, "dislikes": 23, "amei": 67},
    {"likes": 45, "dislikes": 16, "amei": 79},
    {"likes": 63, "dislikes": 32, "amei": 55},
    {"likes": 72, "dislikes": 21, "amei": 93},
    {"likes": 85, "dislikes": 24, "amei": 76}
]

class Comentario:
    
    def __init__(self, likes: int, dislikes: int, amei: int, id: int) -> None:
        self.likes = likes
        self.dislikes = dislikes
        self.amei = amei
        self.id = id
        self.esquerda = None
        self.direita = None
        


class Arvore_Comentarios:
    def __init__(self) -> None:
        self.raiz = None        
        self.comentarios_ordenados_likes = []
        self.comentarios_ordenados_dislikes = []
        self.comentarios_ordenados_amei = []
    
    def adicionar_comentario(self, comentario):
        if not self.raiz:
            self.raiz = comentario
            return
            
        ponteiro_varredor = self.raiz
        while ponteiro_varredor:
            if comentario.likes >= ponteiro_varredor.likes:
                if ponteiro_varredor.direita:
                    ponteiro_varredor = ponteiro_varredor.direita
                else:
                    ponteiro_varredor.direita = comentario
                    break
            else:
                if ponteiro_varredor.esquerda:
                    ponteiro_varredor = ponteiro_varredor.esquerda
                else:
                    ponteiro_varredor.esquerda = comentario
                    break
            
    def print_comentarios_ordenados_likes(self) :        
        self.get_comentarios_por_likes(self.raiz)
        
        for comentario in self.comentarios_ordenados_likes:
            print(f"Id: {comentario.id}\t|\tLikes:{comentario.likes}\t|\tDislikes: {comentario.dislikes}\t|\tAmei: {comentario.amei}")   
            
    def print_comentarios_ordenados_dislikes(self) :        
        self.ordena_comentarios_por_dislikes(self.raiz)
        
        for comentario in reversed(self.comentarios_ordenados_dislikes):
            print(f"Id: {comentario.id}\t|\tLikes:{comentario.likes}\t|\tDislikes: {comentario.dislikes}\t|\tAmei: {comentario.amei}") 
            
    def print_comentarios_ordenados_amei(self) :        
        self.ordena_comentarios_por_amei(self.raiz)
        
        for comentario in reversed(self.comentarios_ordenados_amei):
            print(f"Id: {comentario.id}\t|\tLikes:{comentario.likes}\t|\tDislikes: {comentario.dislikes}\t|\tAmei: {comentario.amei}")     
    
    def get_comentarios_por_likes(self, node):
        #realiza varredura em ordem invertida (direita, node, esquerda) para pegar comentários por ordem decrescente de likes
        if node.direita:
            self.get_comentarios_por_likes(node.direita)
        self.comentarios_ordenados_likes.append(node)
        if node.esquerda:
            self.get_comentarios_por_likes(node.esquerda)
            
    def insercao_binaria_dislikes(self, node):
        inicio, fim = 0, len(self.comentarios_ordenados_dislikes)
        
        if fim == 0:
            self.comentarios_ordenados_dislikes.append(node)
            return
       

        while inicio <= fim:
            meio = (inicio+fim)//2         
            
            if node.dislikes < self.comentarios_ordenados_dislikes[meio].dislikes:                
                if meio-1>=0:
                    if node.dislikes > self.comentarios_ordenados_dislikes[meio-1].dislikes:
                        self.comentarios_ordenados_dislikes.insert(meio, node)
                        break
                    fim = meio
                    continue
                self.comentarios_ordenados_dislikes = [node].append(self.comentarios_ordenados_dislikes)       
 
            elif node.dislikes > self.comentarios_ordenados_dislikes[meio].dislikes:
                if meio+1<=len(self.comentarios_ordenados_dislikes)-1:
                    
                    if node.dislikes < self.comentarios_ordenados_dislikes[meio+1].dislikes:
                        self.comentarios_ordenados_dislikes.insert(meio+1, node)
                        break
                    
                    inicio = meio
                    continue
                
                self.comentarios_ordenados_dislikes.append(node)
                break
            
            else:
                self.comentarios_ordenados_dislikes.insert(meio, node)
                break
            
    def ordena_comentarios_por_dislikes(self, node):
        if node.esquerda:
            self.ordena_comentarios_por_dislikes(node.esquerda)
        self.insercao_binaria_dislikes(node)
        if node.direita:
            self.ordena_comentarios_por_dislikes(node.direita)
            
    def ordena_comentarios_por_amei(self, node):
        if node.esquerda:
            self.ordena_comentarios_por_amei(node.esquerda)
        self.insercao_binaria_amei(node)
        if node.direita:
            self.ordena_comentarios_por_amei(node.direita)
            
    def insercao_binaria_amei(self, node):
        inicio, fim = 0, len(self.comentarios_ordenados_amei)     
        
        if fim == 0:
            self.comentarios_ordenados_amei.append(node)
            return
       

        while inicio <= fim:
            meio = (inicio+fim)//2         
            if node.amei < self.comentarios_ordenados_amei[meio].amei:                
                if meio-1>=0:
                    if node.amei > self.comentarios_ordenados_amei[meio-1].amei:
                        self.comentarios_ordenados_amei.insert(meio, node)
                        break
                    fim = meio
                    continue
                self.comentarios_ordenados_amei.insert(meio, node)       
 
            elif node.amei > self.comentarios_ordenados_amei[meio].amei:
                if meio+1<=len(self.comentarios_ordenados_amei)-1:
                    
                    if node.amei < self.comentarios_ordenados_amei[meio+1].amei:
                        self.comentarios_ordenados_amei.insert(meio+1, node)
                        break
                    
                    inicio = meio
                    continue
                
                self.comentarios_ordenados_amei.append(node)
                break
            
            else:
                self.comentarios_ordenados_amei.insert(meio, node)
                break
        

arvore_comentarios = Arvore_Comentarios()
id_cont = 0
for comentario in comentarios:   
    id_cont += 1
    arvore_comentarios.adicionar_comentario(Comentario(comentario['likes'], comentario['dislikes'], comentario['amei'], id_cont))
    
# arvore_comentarios.imprime_comentarios_ordenados()
print("\n ----- Ordenação por likes ----- \n")
arvore_comentarios.print_comentarios_ordenados_likes()
print("\n ----- Ordenação por dislikes ----- \n")
arvore_comentarios.print_comentarios_ordenados_dislikes()
print("\n ----- Ordenação por amei ----- \n")
arvore_comentarios.print_comentarios_ordenados_amei()