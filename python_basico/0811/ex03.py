nomeCompleto = input("Digite seu nome completo: ")

primeiroNome = nomeCompleto[0:nomeCompleto.find(' ')]
ultimoNome = nomeCompleto[nomeCompleto.rfind(' ')+1:]

email = primeiroNome.lower() + "." + ultimoNome.lower() + "@gmail.com"

print(f"O email montado é {email}")