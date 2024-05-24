'''
17. Escribir un programa que muestre números del 0 al 30 uno debajo de otro.
● Cuando los números sean 3, 8, 17, 26 debe mostrar el mensaje “saltando
instrucciones con(xxxxxxxxxxxxx el nombre de la instrucción que permite realizar
saltos en un bucle) llegue al número 3 o 8 o 17 o 26 ”
● Cuando los números sean mayor a 25 debe preguntar si continúa o sale del conteo
(por ejemplo presione Presione: 'S' para salir , cualquier otra tecla para continuar)
○ Si presiona cualquier tecla el programa seguirá su curso
○ Si presiona S, terminará el programa, antes de terminar debe mostrar a qué
número de conteo llegó .
'''
numero = 0
while True:
    print(numero)
    if numero == 3 or numero == 8 or numero == 17 or numero == 26:
        print('Saltando instrucciones con (continue) llegue al numero 3 o 8 o 17 o 26')
        numero += 1
        continue
    if numero >= 25:
        opcion = input('Ingrese "S" para dejar de contar, cualquier otra tecla para salir: ').upper()
        if opcion == 'S':
            break
        else:
            pass
        
    if numero == 30:
        break
    numero += 1
    