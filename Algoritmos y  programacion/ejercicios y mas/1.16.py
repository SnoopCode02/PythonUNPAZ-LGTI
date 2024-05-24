'''
16. Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la
cuenta atrás desde ese número hasta cero separados por comas. (Investigue cómo mostrar
datos con print en la misma línea de texto), Si se anima trate de no imprimir la última coma
después del 0.
Ejemplo: 5
5,4,3,2,1,0,
5,4,3,2,1,0
'''
def es_entero_positivo():
    while True:
        numero = input('Ingrese un numero: ')
        try:
            int(numero)
            return int(numero)
        except ValueError:
            print('¡Por favor ingrese un numero entero positivo!')

    while True:
        if numero >= 0:
            break
        else:
            print('¡Por favor ingrese un numero entero positivo!')
            
num = es_entero_positivo()
while True:
    if num != 0:
        print(f'{num},', end = '')
        num -= 1
    else:
        print(f'{num}')
        break


