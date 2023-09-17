""" 
5.1. Realiza un programa principal que lea tres números enteros por teclado, los
almacene en tres variables (x, y, z) y llame a una función llamada máximo(), con
tres argumentos, que devuelva el máximo de estos tres valores.
"""
def maximo(x,y,z):
    maximo = x
    if y > maximo:
        maximo = y
    elif z > maximo:
        maximo = z
    return maximo

x = int(input("Ingrese el numero 'X': "))
y = int(input("Ingrese el numero 'Y': "))
z = int(input("Ingrese el numero 'Z': "))

print(f"El maximo de los 3 numeros es: {maximo(x,y,z)}")