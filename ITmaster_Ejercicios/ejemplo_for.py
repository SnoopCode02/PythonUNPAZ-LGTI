"""
Leer 10 numeros desde el teclado.
Mostrar la suma. 
"""
suma = 0
for contador in range(10): 
    
    
    numero = int(input("numeros: "))
    suma += numero
print(f"La suma es: {suma}")


