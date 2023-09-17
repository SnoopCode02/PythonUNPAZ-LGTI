## Ejercicio 032

# Una remisería requiere un sistema que calcule el precio de un viaje a partir de la cantidad de km que desea recorrer el usuario.
# Tiene la siguiente tarifa: 

#- Viaje mínimo $50  MINIMO

#- Si recorre entre 0 y 10km: $20/km  MEDIO

#- Si recorre 10km o más: $15/km  EXTENSO


# Escribir un programa que permita ingresar la cantidad de km que desea recorrer el usuario y muestre el precio del viaje.
MINIMO = 50
MEDIO = 20
EXTENSO = 15
km = ""
flag = False
while not flag:
    km = input("Ingrese la cantidad de km a recorrer: ")
    if km .isdigit():
        km = int(km)
        flag = True
    else: 
        print("Ingrese un valor numerico positivo.")
medio = km * MEDIO
extenso = km * EXTENSO
if 0 < km <= 2:
    print(f"El costo de su viaje es de: {MINIMO}$")
elif 2 < km <= 10:
    print(f"El costo de su viaje es de: {medio}$")
else: 
    print(f"El costo de su viaje es de: {extenso}$")
