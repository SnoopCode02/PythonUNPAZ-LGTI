"""
3.5. Crear un programa con un vector de 5 posiciones que lea todas las posiciones y
luego imprima el doble de los valores leídos en cada una de sus posiciones.
"""
import array as a
TAM = 5 
numeros = a.array('i', range(TAM))

for i in range(TAM):
    numeros[i] = int(input(f"ingrese el {i+1}° numero: "))

doble_numeros = a.array('i', range(TAM))

for i in range(TAM):
    doble_numeros[i] = numeros[i]*2

print("Arreglo original:")
for i in numeros:
    print(i, end=" ")
print("\nArreglo doble de valores:")
for i in doble_numeros:
    print(i, end=" ")

