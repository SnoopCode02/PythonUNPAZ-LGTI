## Ejercicio 041

### Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el máximo.
import random

num_max = 0

numero = None

while numero != 0:
    numero = random.randint(0,348)#int(input("Ingrese un numero: "))
    if num_max < numero:
        num_max = numero
        
print(f"El numero mayor es: {num_max}")





