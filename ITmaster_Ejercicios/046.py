## Ejercicio 046

### Escribir un programa que a partir de un número entero cant ingresado por el usuario permita cargar por teclado cant números enteros. La computadora debe mostrar cuál fue el mayor número y en qué posición apareció.

num_mayor = 0
posc = 0
cant_posc = int(input("Ingrese la cantidad de numeros a ingresar: "))
for posicion in range(1,cant_posc +1):
   num = int(input(f"Ingrese el {posicion}° numero: "))
   if num_mayor <  num:
       num_mayor = num
       posc = posicion

print(f"El numero mayor es: {num_mayor} y aparecio en la posicion: {posc}")