import os

musicas = [
    {"nome": "Smells Like Teen Spirit", "cantor": "Nirvana"},
    {"nome": "Stairway to Heaven", "cantor": "Led Zeppelin"},
    {"nome": "Back in Black", "cantor": "AC/DC"},
    {"nome": "Sweet Child o' Mine", "cantor": "Guns N' Roses"},
    {"nome": "Paint It Black", "cantor": "The Rolling Stones"},
    {"nome": "Livin' on a Prayer", "cantor": "Bon Jovi"},
    {"nome": "Sweet Emotion", "cantor": "Aerosmith"},
    {"nome": "Eye of the Tiger", "cantor": "Survivor"},
    {"nome": "Don't Stop Believin'", "cantor": "Journey"},
    {"nome": "Hotel California", "cantor": "Eagles"},
    {"nome": "Hello", "cantor": "Adele"},
    {"nome": "Blinding Lights", "cantor": "The Weeknd"},
    {"nome": "Uptown Funk", "cantor": "Mark Ronson ft. Bruno Mars"},
    {"nome": "Despacito", "cantor": "Luis Fonsi ft. Daddy Yankee"},
    {"nome": "Wannabe", "cantor": "Spice Girls"},
    {"nome": "Havana", "cantor": "Camila Cabello ft. Young Thug"},
    {"nome": "Imagine", "cantor": "John Lennon"},
    {"nome": "Rolling in the Deep", "cantor": "Adele"},
    {"nome": "Billie Jean", "cantor": "Michael Jackson"}
]

class Musica:
    def __init__(self, musica):
        self.anterior = None
        self.proxima = None
        self.nome = musica['nome']
        self.cantor = musica['cantor']
        
    def __str__(self) -> str:
        return f"Música: {self.nome} | Cantor: {self.cantor}"
    

class Playlist:
    def __init__(self, musica):
        self.inicio = musica
        self.fim = musica
        musica.proxima = self.inicio
        musica.anterior = self.fim
        self.musica_atual = musica
        self.qtde_musicas = 1


    def adiciona_musica(self, musica):
        musica.anterior = self.fim
        self.fim.proxima = musica
        self.fim = musica
        self.fim.proxima = self.inicio
        self.inicio.anterior = self.fim
        self.qtde_musicas += 1
        print("Música adicionada com sucesso!")
        
    def listar_musicas(self):
        varredor = self.inicio
        for i in range(self.qtde_musicas):
            print(varredor)
            varredor = varredor.proxima
        input("Aperte uma tecla para continuar...")
        
    def remover_musica(self, nome_musica):
        varredor = self.inicio
        while varredor:
            if varredor.proxima == None:
                print("Música não encontrada. Nada foi alterado")
                break
            if varredor.nome == nome_musica:
                if varredor.nome == self.inicio.nome:
                    self.inicio = self.inicio.proxima
                if varredor.nome == self.fim.nome:
                    self.fim = self.fim.anterior
                varredor.anterior.proxima = varredor.proxima
                varredor.proxima.anterior = varredor.anterior
                self.qtde_musicas-=1
                break
            varredor = varredor.proxima

    def passar_musica(self):
        self.musica_atual = self.musica_atual.proxima
        
    def voltar_musica(self):
        self.musica_atual = self.musica_atual.anterior

#Iniciando a lista
playlist = Playlist(Musica({"nome": "Bohemian Rhapsody", "cantor": "Queen"}))

for musica in musicas:
    playlist.adiciona_musica(Musica(musica))
    

while True:
    os.system("clear")
    print(f"Música tocando: \n{playlist.musica_atual}\n")
    opcao = int(input("Selecione uma opção:\n1 - Pular Música\n2 - Voltar Música\n3 - Listar Músicas na Playlist\n4 - Adicionar Música\n5 - Remover Música\n0 - Sair\n"))
    match opcao:
        case 1:
            playlist.passar_musica()
        case 2:
            playlist.voltar_musica()
        case 3:
            playlist.listar_musicas()
        case 4:
            nome = input("Insira o nome da música: ")
            cantor = input("Insira o nome do cantor: ")
            playlist.adiciona_musica(Musica({"nome": nome, "cantor": cantor}))
            input("Aperte uma tecla para continuar...")
        case 5:
            playlist.remover_musica(input("Insira o nome da música: "))
        case 0:
            break



    