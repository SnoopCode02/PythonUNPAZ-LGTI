"""
Leer numeros hasta que se ingrese un cero
mostrar la suma
"""

#antes
sumador = 0
numero = int(input("Numero: "))
while numero != 0:
    #durante (para cada dato)
    
    sumador += numero
    
    numero = int(input("Numero: "))
#despues
print(f"La suma es: {sumador}")

