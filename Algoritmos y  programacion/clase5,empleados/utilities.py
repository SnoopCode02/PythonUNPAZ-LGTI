menu_principal = """
1. Cargar empleados.
2. Listar empleados activos.
3. Listar empleados inactivos.
4. Buscar empleado.
5. Modificar empleado.
6. Borrar empleado.
7. Terminar programa.
"""
def mostrar_menu():
    print(menu_principal)

menu_buscador = """
Menu Buscador 
1. Buscar por ID.
2. Buscar por Nombre y Apellido.
3. Buscar por categoria.
4. Volver al menu principal
"""
def mostrar_buscador():
    print(menu_buscador)
    
menu_modificador = """
Menu Modificador
1. Modificar Nombre.
2. Modificar apellido:
3. Modificar Categoria.
4. volver al menu principal.
"""

def mostrar_modificador():
    print(menu_modificador)

def es_entero(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
            return int(numero)
        except ValueError:
            print("¡Por favor ingrese un numero entero!")

def es_flotante(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            float(numero)
            return float(numero)
        except ValueError:
            print("¡Por favor ingrese un numero!")