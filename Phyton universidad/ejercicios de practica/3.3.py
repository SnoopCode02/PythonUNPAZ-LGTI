"""
3.3. Diseñe un programa que lea un vector de 10 posiciones, luego determine la primera
posición que contenga un número múltiplo de 3. En caso que no lo contenga deberá
informar por pantalla “No existe”
"""
import array as pepe
import random
TAM = 10
numeros = pepe.array('i', range(TAM))

for i in range(TAM):
    numeros[i] = random.randint(2,2) #int(input(f"Ingrese el {i+1}° numero: "))
print(numeros)

posc = TAM + 1
for i in range(TAM):
    if numeros[i] % 3 == 0 and posc > i:
        posc = i
        print(f"La primera posicion que contiene un numero multiplo de 3 es la numero: {posc}")
if posc == TAM+1:
    print("no se cargaron numeros multiplos de 3")
    




