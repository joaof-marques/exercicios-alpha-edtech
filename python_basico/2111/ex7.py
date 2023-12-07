import random

fitaDNA = ''
basesNitrogenadas = ('A', 'C', 'G', 'T')

for i in range(10000000):
    baseRandomica = random.randint(0, 3)
    fitaDNA += basesNitrogenadas[baseRandomica]
    
print(fitaDNA)