"""
Ejercicio 025

Para acceder a cierta atracción, alcanza con que se
cumpla solamente una de las siguientes condiciones:
ser __mayor__ de 6 años o medir __más__ de 1,50 metros.
Escribir un programa en Python que solicite al
usuario su edad y estatura, y que determine si cumple
con los requisitos para subir a la atracción. Si cumple
con al menos una de las condiciones, el programa debe
imprimir "¡Puede acceder!" en la pantalla. Si no cumple
con ninguna de las condiciones, el programa debe imprimir
un mensaje que lo indique.

"""
edad = int(input("Ingrese su edad?: "))
altura = float(input("Ingrese su estatura: "))

if edad >= 6 or altura >= 1.50:
    print("Puedes pasar a la atraccion")
else:
    if edad < 6:
        print("Lo siento, eres demasiado joven para acceder.")
    if altura < 1.50:
        print("Lo siento, eres demasiado bajo para acceder.")

