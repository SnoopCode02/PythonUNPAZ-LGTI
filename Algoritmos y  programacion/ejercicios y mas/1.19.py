'''
19. Escribir un programa que solicite un número entero positivo, que muestre los múltiplos de 5
que existen entre el número ingresado y su multiplicación por 30. por ejemplo: entre 3 y
(3*30)
'''
def es_entero_positivo(sTr):
    while True:
        numero = input(sTr)
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
            
num = es_entero_positivo('Ingrese un numero entero positivo: ')

for i in range(num, num*30 + 1):
    if i % 5 == 0:
        print(f'{i},', end = '')
    
    

