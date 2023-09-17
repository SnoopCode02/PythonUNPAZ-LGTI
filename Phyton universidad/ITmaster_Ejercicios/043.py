## Ejercicio 043

### Escribir un programa que lea números enteros hasta que se la suma de éstos sea mayor que 100, y muestre la cantidad de números ingresados.
import random
num = 0
sum = 0
cont = 0
while sum < 100:
    num = random.randint(-500,500)
    sum += num
    cont += 1

print(f"La cantidad de numeros ingresados es {cont}")