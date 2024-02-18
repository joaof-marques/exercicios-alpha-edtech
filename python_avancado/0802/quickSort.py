def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivô = array[-1]
        menores = [x for x in array[:-1] if x <= pivô]
        maiores = [x for x in array[:-1] if x > pivô]
        print(f'{menores} | {pivô} | {maiores}')
        return quicksort(menores) + [pivô] + quicksort(maiores)

array_exemplo = [2, 4, 1, 9, 3, 8, 7, 9, 6, 5]
array_ordenado = quicksort(array_exemplo)
print(f'ARRAY ORDENADO: {array_ordenado}')