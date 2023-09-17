## Ejercicio 047

### Escribir un programa que permita validar la nota de un examen. Se espera que la nota que el usuario ingrese sea un número comprendido entre 0 y 10.  
### La misma debe ser ingresada tantas veces como sea necesario hasta que quede comprendida dentro del rango indicado.
import random
LIM_INF = 0
LIM_SUP = 10

flag = False

while not flag:
    nota = int(input(f"Ingrese una nota: "))#random.randint(-10,20)
    
    if LIM_INF < nota < LIM_SUP:
        print(nota)
        flag = not flag
