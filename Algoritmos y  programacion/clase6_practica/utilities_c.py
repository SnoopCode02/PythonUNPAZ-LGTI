menu = """
1. Ingresar libros a la biblioteca.
2. Buscar libro.
3. Mostrar libros de un autor en especifico.
4. Salir del programa.
"""

def mostrar_menu():
    print(menu)
    
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
