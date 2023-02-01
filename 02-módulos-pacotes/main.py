from operações.soma import somar
from operações.multiplica import multiplicar
from math import floor

print("\n", end="")
temperatura = int(input("Digite a temperatura em grau Celsius: "))

fahrenheit = multiplicar(temperatura, 1.8)
fahrenheit = somar(fahrenheit, 32)
fahrenheit = floor(fahrenheit)

kelvin = somar(temperatura, 273.15)

print("\n", end="")
print(f"A temperatura em Fahrenheit é {fahrenheit} °F.")
print(f"A temperatura em Kelvin é {kelvin:.2f} K.")