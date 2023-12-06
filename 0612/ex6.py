def avaliar_condicao (valor, callback_true, callback_false):
    if valor:
        callback_true()
    else: callback_false()
    
def verdadeiro ():
    print("O valor é verdadeiro")

def falso ():
    print("O valor é falso")
    
avaliar_condicao(True, verdadeiro, falso)
avaliar_condicao(False, verdadeiro, falso)
avaliar_condicao([], verdadeiro, falso)
avaliar_condicao([1], verdadeiro, falso)

