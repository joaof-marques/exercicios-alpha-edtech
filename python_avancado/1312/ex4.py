estoque = [{"fruta":"abacate","quantidade": 10}, {"fruta":"abacaxi","quantidade": 30}, {"fruta":"maçã","quantidade": 8}, {"fruta":"banana","quantidade": 12}]

#Essa opção retorna o objeto inteiro que tem a menor quantidade
fruta_menor_quantidade = min(estoque, key= lambda x:x["quantidade"])

#Se quisermos acessar apenas o valor, temos que chamar a key "quantidade" desse objeto:
print(fruta_menor_quantidade)
print(fruta_menor_quantidade["quantidade"])