def verificaPalindromo (texto):
    if len(texto) in [0,1]:
        return True
    elif texto[0] == texto[len(texto)-1]:
        return verificaPalindromo(texto[1:len(texto)-1])
    else: 
        return False
    
    
def ePalindromo(texto):
    texto = texto.replace(" ", "").lower()
    if verificaPalindromo(texto):
        print(f"O texto '{texto}' é palíndromo!")
    else: print(f"O texto '{texto}' não é palíndromo!")
    
    
ePalindromo("arara")
ePalindromo("A base do teto desaba")
ePalindromo("Socorram me subi no onibus em Marrocos")
ePalindromo("teste")
ePalindromo("Texto nao palindromo")

