## Ejercicio 042

### Escribir un programa que lea números enteros hasta que se ingrese un 0, y muestre el promedio de los números ingresados.

def validar_entero(cadena):
    es = False
    for caracter in cadena:
        if not caracter.isdigit() and caracter == '-':
            return False
        else:
            return True
            

def leer_entero(cartel):
    todo_ok = False
    while todo_ok == False:
        numero = input(cartel)
        
        if validar_entero(numero) == True:
            todo_ok = True
        else:
            print(f"{numero} No es un numero!.")
    return int(numero)        

def main():
    suma = 0
    cont = 0
    numero = leer_entero("Ingrese un numero: ")
    while numero != 0:
        cont += 1
        suma += numero
        numero = leer_entero("Ingrese un numero: ")
    prom = suma/cont
    print(f"Promedio: {prom}")
main()

