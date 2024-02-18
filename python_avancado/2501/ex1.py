from random import randint

class Paciente:
    def __init__(self) -> None:
        self.tempo_espera = 0
    
    def __str__(self) -> str:
        return f"Paciente senha: {self.senha_fila} | Tempo de espera atual: {self.tempo_espera} minutos"
    
    def verificar_tempo_espera(self):
        return f"O tempo de espera do paciente {self.senha_fila} foi de {self.tempo_espera} minutos"
    
class Hospital:
    def __init__(self) -> None:
        self.fila = []
        self.paciente_em_atendimento = None
        self.contador_paciente = 0
        
    def adicionar_paciente_fila (self, paciente):
        self.fila.append(paciente)
        self.contador_paciente += 1
        paciente.senha_fila = self.contador_paciente
        
    def chamar_paciente_para_atendimento (self):
        if self.verificar_fila_vazia():
            print("Não há pacientes na fila")
            return
        
        self.paciente_em_atendimento = self.fila[0]
        self.paciente_em_atendimento.tempo_atendimento = randint(1, 10)        
        self.fila.pop(0)
        self.atualizar_tempo_espera_fila(self.paciente_em_atendimento.tempo_atendimento)
        
    def identificar_paciente_atendimento (self):
        print(f"Paciente em atendimento. Senha fila: {self.paciente_em_atendimento.senha_fila}")
            
    def verificar_fila_vazia(self):
        if len(self.fila) == 0:
            return True
        return False
    
    def listar_paciente_fila(self):
        for paciente in self.fila:
            print(paciente)

    def atualizar_tempo_espera_fila(self, tempo_atendimento):
        for paciente in self.fila:
            paciente.tempo_espera += tempo_atendimento
        
hospital = Hospital()

#Inicio a fila com 20 pois é o pior cenário para o 20º paciente
for _ in range(20):
    hospital.adicionar_paciente_fila(Paciente())
    
#Chamo 19 para atendimento para gerar o tempo de atendimento de cada um
#Ao final, isso também dará o tempo de espera do 20º, que no pior caso é de 190 min
for _ in range(19):
    hospital.chamar_paciente_para_atendimento()


hospital.listar_paciente_fila()


#É legal notar que mesmo os tempos sendo aleatórios, normalmente varia próximo à 100 minutos
#É o Teorema do Limite Central
# https://www.youtube.com/watch?v=j50_3TCguls&ab_channel=UniversoProgramado