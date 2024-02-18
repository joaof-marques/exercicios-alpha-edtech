import logging
from datetime import datetime

logging.basicConfig(filename='log_Pessoas.log', encoding='utf-8', level=logging.DEBUG)

class Pessoa:
    tipo = 'pessoa'
    def __init__ (self, nome):
        self.nome = nome
        
        time = datetime.now()
        logging.info(f"{time.day}/{time.month}/{time.year} {time.hour}:{time.minute} - Objeto Pessoa({nome}) gerado ")
        
    def __del__(self):
        time = datetime.now()
        logging.info(f"{time.day}/{time.month}/{time.year} {time.hour}:{time.minute} - Objeto Pessoa({self.nome}) excluído.")    
        
    def get_nome (self):
        return self.__nome
    
    @staticmethod
    def set_tipo():
        Pessoa.tipo = "outro tipo"
        
        time = datetime.now()
        logging.info(f"{time.day}/{time.month}/{time.year} {time.hour}:{time.minute} - Tipo da classe Pessoa alterado para {Pessoa.tipo} ")
    
    
joao = Pessoa('João Marques')
Pessoa.set_tipo()
