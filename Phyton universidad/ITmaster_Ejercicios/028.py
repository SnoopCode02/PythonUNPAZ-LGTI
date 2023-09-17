## Ejercicio 028

#Crear un programa que pida un número de mes (ejemplo 4) y escriba el nombre del mes en letras ("abril"). Verificar que el mes sea válido e informar en caso que no lo sea.

import random

#mes = int(input("Digame el numero de un mes: "))
mes = random.randint(1,12)
mes_correcto = 1 <= mes <= 12
if mes_correcto:
    if mes == 1:
        print("El mes 1 es enero: ")
    elif mes == 2:
        print("El mes 2 es febrero: ")
    elif mes == 3:
        print("El mes 3 es marzo: ")
    elif mes == 4:
        print("El mes 4 es abril: ")
    elif mes == 5:
        print("El mes 5 es mayo: ")
    elif mes == 6:
        print("El mes 6 es junio: ")
    elif mes == 7:
        print("El mes 7 es julio: ")
    elif mes == 8:
        print("El mes 8 es agosto: ")
    elif mes == 9:
        print("El mes 9 es septiembre: ")
    elif mes == 10:
        print("El mes 10 es octubre: ")
    elif mes == 11:
        print("El mes 11 es noviembre: ")
    else:
        print("El mes 12 es diciembre: ")
else:
    print("Opcion invalida, Los meses van del 1 al 12")
    