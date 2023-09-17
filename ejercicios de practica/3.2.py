"""
3.2. Desarrollar un algoritmo que permita la carga de un vector de 10 posiciones.
Generar una rutina que transcriba el contenido del vector a otro vector en orden
inverso.
"""


import array as a
TAM = 10
num = a.array('i',range(TAM))

for i in range(TAM):
    num[i] = int(input("Ingrese un num: "))


array_invertido = a.array('i', range(TAM))
array_invertido_indice = TAM -1 
for i in range(TAM):
    array_invertido[array_invertido_indice] = num[i]
    array_invertido_indice -= 1
    
print("arreglo original:")
for i in num:
    print(i,end=" ")
print("\n,Arreglo invertido")
for i in array_invertido:
    print(i, end=" ")


