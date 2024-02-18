def merge_sort(array):
    if len(array) > 1:
        meio = len(array) // 2
        esquerda = array[:meio]
        direita = array[meio:]

        # Ordena as metades
        print(f'{esquerda} | {direita}')
        merge_sort(esquerda)
        merge_sort(direita)

        # Mescla as metades ordenadas
        i = j = k = 0

        # Enquanto houver elementos em ambas as metades
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                array[k] = esquerda[i]
                i += 1
            else:
                array[k] = direita[j]
                j += 1
            k += 1

        # Verifica se ainda há elementos na metade esquerda
        while i < len(esquerda):
            array[k] = esquerda[i]
            i += 1
            k += 1

        # Verifica se ainda há elementos na metade direita
        while j < len(direita):
            array[k] = direita[j]
            j += 1
            k += 1

    return array

# Exemplo de uso
array_exemplo = [38, 27, 43, 3, 9, 82, 10]
array_ordenado = merge_sort(array_exemplo)
print(f'ARRAY ORDENADO: {array_ordenado}')