grausCelsius = float(input("Insira a temperatura para conversão (em graus Celsius): "))

grausFahrenheit = (grausCelsius * 1.8) + 32
grausKelvin = grausCelsius + 273.15

print(f"{grausCelsius:.2f} °Celsius representam {grausFahrenheit:.2f} °Fahrenheit e {grausKelvin:.2f} °Kelvin")