def converte_string_int():
    string = input("Insira uma string")
    
    try:
        string = int(string)
    except ValueError:
        return "Não foi possível converter a string em int pois os caracteres são não numéricos"
    
    return string**2

print(converte_string_int())