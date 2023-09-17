"""
Desarrollar un algoritmo lea desde teclado un vector de 10 posiciones y que detecte
los elementos repetidos de un vector y los reemplace con un 0 y los deposite en
otro vector.
"""
import array as a
TAM = 10 
array = a.array('i', range(TAM))

for i in range(TAM):
    array[i] = int(input(f"ingrese el {i+1}° numero: "))

array_copia = a.array('i')

for numero in array:
    if array.count(numero) > 1:
        array_copia.append(0)
    else:
        array_copia.append(numero)

print("Arreglo original")     
for i in range(TAM):
    if i == 0:
        str = f"[{array[i]}, "
    elif i == TAM - 1:
        str = f"{array[i]}]"
    else:
        str = f"{array[i]}, "
    print(str, end="")
print("\nArreglo copia")
for i in range(TAM):
    if i == 0:
        str = f"[{array_copia[i]}, "
    elif i == TAM - 1:
        str = f"{array_copia[i]}]"
    else:
        str = f"{array_copia[i]}, "
    print(str, end="")