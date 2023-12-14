import time
import sys

tempo_inicio_lista = time.time()
lista_quadrados = [x**2 for x in range(1, 6)]
tempo_final_lista = time.time()
execucao_lista = tempo_final_lista-tempo_inicio_lista

tempo_inicio_generator = time.time()
generator_quadrados = (x**2 for x in range(1, 6))
tempo_final_generator = time.time()
execucao_generator = tempo_final_generator-tempo_inicio_generator

   

print(f"Valores lista: {lista_quadrados}\nTempo de Execução: {execucao_lista}\nTamanho em bytes: {sys.getsizeof(lista_quadrados)}")

print(f"Valores generator: {generator_quadrados}\nTempo de Execução: {execucao_generator}\nTamanho em bytes: {sys.getsizeof(generator_quadrados)}")