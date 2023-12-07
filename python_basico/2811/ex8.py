def teste_kargs(arg1, arg2, **kwargs):
    print(arg1)
    print(arg2)
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        
        
# teste_kargs("João", "Marques", )
teste_kargs("carro", 100, nome="jose", chave="teste")
teste_kargs("carro", 100, nome="jose", chave="teste", outraChave="brasil", oo="python")