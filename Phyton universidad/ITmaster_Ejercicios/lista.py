from array import *
ARRAY_TAM=10
LIMITE_PUNTUACION=10
arreglo_original=array('i',range(ARRAY_TAM))
for i in range(ARRAY_TAM):
    arreglo_original[i]=int(input("Alumno {} Ingrese la calificación: ".format(i+1)))
arreglo_puntuaciones=array('i',range(LIMITE_PUNTUACION))

for i in range(LIMITE_PUNTUACION):
    cont=0
    for calificacion_actual in arreglo_original:
        if i+1==calificacion_actual:
            cont+=1
    arreglo_puntuaciones[i]=cont

print("Calidad\tFrecuencia")
for i in range(LIMITE_PUNTUACION):
    print("%i\t\t%i" % (i + 1, arreglo_puntuaciones[i]))
