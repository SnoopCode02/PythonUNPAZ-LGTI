from array import *
ARRAY_TAM=5
mi_arreglo=array('i',range(ARRAY_TAM))
for i in range(ARRAY_TAM):
    temp=int(input("Ingrese el número {}: ".format(i+1)))
    mi_arreglo[i]=temp

arreglo_invertido=array('i',range(ARRAY_TAM))
arreglo_invertido_indice=ARRAY_TAM-1
for i in range(ARRAY_TAM):
    arreglo_invertido[arreglo_invertido_indice]=mi_arreglo[i]
    arreglo_invertido_indice-=1

print("Arreglo original:")
for i in mi_arreglo:
    print(i, end=" ")
print("\nArreglo invertido:")
for i in arreglo_invertido:
    print(i, end=" ")