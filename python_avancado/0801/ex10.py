nome_poligonos = {
    3: 'Triângulo',
    4: 'Retângulo',
    5: 'Pentágono',
    6: 'Hexágono',
    7: 'Heptágono',
    8: 'Octógono',
    9: 'Eneágono',
    10: 'Decágono'
}

class Exclusao_triangulo (Exception):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
        super().__init__(mensagem)

class Poligono:
    def __init__(self, qtde_lados:int=3, cor_interna:str = 'Branco') -> None:
        self.qtde_lados = qtde_lados
        self.cor_interna = cor_interna
        if qtde_lados>10:
            self.nome = f'Polígono genérico de {qtde_lados} lados'
        elif qtde_lados<3:
            print("Tá maluco?")
            exit()
        else: self.nome = nome_poligonos[qtde_lados]
        
    def __del__(self):
        try:
            if self.qtde_lados == 3:
                raise Exclusao_triangulo("Você não pode destruir um Triângulo!")            
        except Exclusao_triangulo as erro:
            print(f'Erro: {erro.mensagem}')

tres_lados = Poligono(3, "Azul")

del tres_lados
    
print("Código continuou")