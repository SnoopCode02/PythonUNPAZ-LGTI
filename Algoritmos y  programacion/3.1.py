"""
1. Dado el siguiente programa trate de resolver cualquier error que pueda
producirse al ejecutarlo, resuelva con excepciones.
"""
#Error comun: ValueError
def introducir_entero_valido(mensaje):
    while True:
        num = input(mensaje).strip()
        try:    
            num = int(num)
            return int(num)    
        except ValueError:
            print(f"El numero: {num} no es un entero, presione enter para continuar.")
            input()
            
resultado= 0
menor = 0
numero_1 = introducir_entero_valido('Introduce un numero: ')
numero_2 = introducir_entero_valido('Introduce un numero: ')
if numero_1 == numero_2:
    print("Los dos números son iguales.")
elif numero_1 < numero_2:
    print(f"El numero {numero_1} es menor que {numero_2}")
    menor = numero_1
else:
    print(f"El numero {numero_2} es menor que {numero_1}")
    menor = numero_2
resultado = numero_2 * numero_1
print(f"El resultado entre {numero_1} * {numero_2} = {resultado}")
for i in range(menor,resultado+1):
    print(i)