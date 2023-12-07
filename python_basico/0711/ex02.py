import math

a = float(input("Insira o valor do lado A (em cm): "))
b = float(input("Insira o valor do lado B (em cm): "))
c = float(input("Insira o valor do lado C (em cm): "))

volume = a * b * c
diagonal = math.sqrt(((a**2)+(b**2)+(c**2)))

print(f"O volume do paraleleípedo é: {volume:.2f} cm³")
print(f"A diagonal desse mesmo paralelepípedo mede: {diagonal:.2f} cm")