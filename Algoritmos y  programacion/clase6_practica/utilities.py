menuprin = """
1. Cargar Matriz.
2. Mostrar Matriz
3. Sumar diagonal.
4. Buscar el maximo.
"""

def mostrar_menu():
    print(menuprin)

def es_entero_mayor_a_cero(str):
    while True:
        num = input(str)
        try:
            int(num)
        except ValueError:
            print('Ingrese un numero entero mayor a 0!!')
            continue
        num = int(num)
        if num > 0:
            return num
        else:
            print('Ingrese un numero entero mayor a 0!!')


def es_entero(str):
    while True:
        num = input(str)
        try:
            int(num)
            return int(num)
        except ValueError:
            print('Ingrese un numero entero!!')

