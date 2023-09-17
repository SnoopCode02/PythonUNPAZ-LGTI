"""
## Ejercicio 005

### Escribir un programa que solicite al usuario ingresar dos notas de un alumno.
El programa debe mostrar por pantalla el promedio de las notas de la siguiente
manera: "Notas: [nota1] , [nota2] ==> promedio: [(nota1+nota2)/2]".
Ejemplo: Si el usuario ingresa 7 y 8, el programa debe mostrar por pantalla:
 "Notas: 7 , 8 ==> promedio: 7.5".
"""
not1 = int(input("Digame la primera nota: "))
not2 = int(input("Digame la segunda nota: "))
print("Notas: {not1};{not2} ==> Su promedio es: %.2f"%((not1+not2)/2))