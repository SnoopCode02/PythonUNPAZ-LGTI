from pilas import *
def ingresar_nombres():
    while True:
        nombre = input('Ingrese un nombre o (enter) salir: ').capitalize()
        if len(nombre) == 0:
            break
        else:
            pila_nombres.apilar(nombre)

def mostrar_menu():
    print(f'''
     ___Menu___
1. Ingresar Nombre.
2. Desapilar Nombre.
3. Salir.
''')
pila_nombres = Pila()
opcion = ""
while True:
    mostrar_menu()
    opcion = input('Ingrese una opcion: ')
    if opcion == "1":
        ingresar_nombres()
    elif opcion == "2":
            pila_nombres.desapilar()
            #print(f'El nombre {pila_nombres[-1]} fue desapilado')
    elif opcion == "3":
        if pila_nombres.tamanio() == 0:
            break
        else:
            pila_nombres.imprimir_al_reves()
            break
    else:
        print('Opcion Incorrecta intente nuevamente')
