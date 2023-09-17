"""
3.4. Crear un programa que lea e imprima el promedio del total de los elementos pares
de un vector de 10 posiciones
"""
import array as a 
TAM = 10 
numeros = a.array('i', range(TAM))

for i in range(TAM):
    numeros[i] = int(input("ingrese num: "))

sumatoria = 0
cont = 0 
for numero in numeros:
    if numero % 2 == 0:
        sumatoria += numero
        cont += 1
if cont != 0:
    print(f"El promedio de numeros pares es: {sumatoria/cont}")
else:
    print("No se ingresaron numeros pares.")





