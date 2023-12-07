populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015

qtdeAnos = 0

while populacaoA < populacaoB:
    populacaoA *= crescimentoA
    populacaoB *= crescimentoB
    print(f"A: {populacaoA}")
    print(f"B: {populacaoB}")
    qtdeAnos += 1 
    
print(qtdeAnos)