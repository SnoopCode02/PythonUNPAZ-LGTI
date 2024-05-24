"""#pedir al usuario el precio original del producto, pedir el porcentaje de descuento y calcular y mostrarlo al usuario

precio = float(input("Ingrese el precio del producto: "))
descuento = float(input("Ingrese el porcentaje de descuento: "))
calculo = precio - ((descuento / 100) * precio)
print(f"Su producto vale: {precio} y tiene un descuento del {descuento}%\nEl precio final del producto es de {calculo}$")
"""
"""Escribir un programa que muestre números del 0 al 30 uno debajo de otro.
● Cuando los números sean 3, 8, 17, 26 debe mostrar el mensaje “saltando
instrucciones con(xxxxxxxxxxxxx el nombre de la instrucción que permite realizar
saltos en un bucle) llegue al número 3 o 8 o 17 o 26 ”
● Cuando los números sean mayor a 25 debe preguntar si continúa o sale del conteo
(por ejemplo presione Presione: 'S' para salir , cualquier otra tecla para continuar)
○ Si presiona cualquier tecla el programa seguirá su curso
○ Si presiona S, terminará el programa, antes de terminar debe mostrar a qué
número de conteo llegó ."""
n = 0
while True:
    n +=1
    if n == 3 or n == 8 or n == 17 or n == 26:
        print(f"""saltando instrucciones con "Pass" llegue al numero: {n}""")
    elif 25 <= n <= 30:
        input
    else: print(n)
    
    
        







