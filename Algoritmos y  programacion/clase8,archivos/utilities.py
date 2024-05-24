menu_p = """
1. Reservar Remis.
2. Confirmar Reserva.
3. Cancelar Reserva.
4. Salir.
"""
def mostrar_menu():
    print(menu_p)


def es_entero(str):
    while True:
        num = input(str)
        try:
            int(num)
            return int(num)
        except ValueError:
            print("Por favor ingrese un numero entero!")