def filtraStringsComCaractere (strings, caractere):
    return [string for string in strings if caractere in string]

print(filtraStringsComCaractere(["nome", "João", "teste", "não", "sim", 'Jeane'], "o"))