def heapify(array, n, i):
    maior = i  # Inicializa o maior como root
    esq = 2 * i + 1     # esquerda = 2*i + 1
    dir = 2 * i + 2     # direita = 2*i + 2

    # Verifica se o filho da esquerda existe e é maior que o root
    if esq < n and array[i] < array[esq]:
        maior = esq

    # Verifica se o filho da direita existe e é maior que o maior até agora
    if dir < n and array[maior] < array[dir]:
        maior = dir

    # Muda o root, se necessário
    if maior != i:
        array[i], array[maior] = array[maior], array[i]  # swap

        # Heapify a raiz.
        heapify(array, n, maior)

def heapSort(array):
    n = len(array)

    # Constrói um maxheap.
    for i in range(n // 2 - 1, -1, -1):
        heapify(array, n, i)

    # Extrai elementos um por um
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]   # swap
        heapify(array, i, 0)

    
# Exemplo de uso
array_exemplo = [12, 11, 6, 13, 5, 6, 7]
heapSort(array_exemplo)
print("Array ordenado:", array_exemplo)