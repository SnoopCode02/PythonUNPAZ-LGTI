## Ejercicio 029

### Escribir un programa que permita Ingresar las notas de los dos parciales de un alumno e indicar si promocionó, aprobó o debe recuperar. Si el valor de la nota no esta entre 0 y 10, debe informar un error.
#- Se promociona cuando las notas de ambos parciales son mayores o iguales a 7.
#- Se aprueba cuando las notas de ambos parciales son mayores o iguales a 4.
#- Se debe recuperar cuando al menos una de las dos notas es menor a 4.

nota1 = int(input("Ingrese la nota del primer parcial: "))
nota2 = int(input("Ingrese la nota del segundo parcial: "))
promociona = nota1 >= 7 and nota2 >= 7
aprueba = 4 <= nota1  and 4 <= nota2 < 7

aprueba2 = 4 <= nota2 and 4 <= nota1 < 7
NOTA_CORRECTA = 0 <= nota1 <= 10 and 0 <= nota2 <= 10
if NOTA_CORRECTA:
    if promociona:
        print("Usted a promocionado")
    elif aprueba:
        print("Usted aprueba pero le falta nota para promocionar.")
    elif aprueba2:
        print("Usted aprueba pero le falta nota para promocionar.")   
else: 
    print("Las notas deben estar entre 0 y 10.")
if NOTA_CORRECTA:
    if 0 <= nota1 < 4:
        print("No aprueba, Debe recuperar el primer parcial")
    elif 0 <= nota2 < 4:
        print("No aprueba, Debe recuperas el segundo parcial.")


