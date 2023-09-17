## Ejercicio 026

### Escribir un programa que permita ingresar la cantidad de invitados a una fiesta y la cantidad de asientos disponibles en el salon. Debes indicar si alcanzan los asientos, Si los asientos no alcanzaran indicar cuántos faltan para que todos los invitados puedan sentarse.
cantidad_invitados = int(input("Ingrese la cantidad de invitados: "))
cantidad_asientos = int(input("Ingrese la cantidad de asientos: "))
asientos_faltantes = cantidad_invitados - cantidad_asientos

if cantidad_asientos >= cantidad_invitados:
    print("Los asientos alcanzan")
else:
    print(f"La cantidad de asientos que faltan son: {asientos_faltantes}")