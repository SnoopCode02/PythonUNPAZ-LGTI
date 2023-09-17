"""
3.6. Crear un programa con un vector ORIGEN de 10 posiciones que lea todas las
posiciones y luego traslade el doble de los valores en aquellas posiciones impares a
otro vector DESTINO.
"""
import array as a
TAM = 10 
array = a.array('i', range(TAM))

for i in range(TAM):
    array[i] = int(input(f"ingrese el {i+1}° numero: "))

array_copia = a.array('i', range(TAM))

for i in range(TAM):
    if i % 2 != 0:
        array_copia[i] = array[i]*2
    else:
        array_copia[i] = array[i]

print("Arreglo original:")
for i in array:
    print(i, end=" ")
print("\nArreglo el doble en posiciones impares:")
for i in array_copia:
    print(i, end=" ")
