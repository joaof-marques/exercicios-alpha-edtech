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
        
doze_lados = Poligono(12, 'Amarelo')
quatro_lados = Poligono(4)

print(doze_lados.nome, doze_lados.cor_interna)
print(quatro_lados.nome, quatro_lados.cor_interna)