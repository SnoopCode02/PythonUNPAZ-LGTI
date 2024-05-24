'''
1. A partir del programa realizado de Pila, Realice un programa a base de menú, con las
opciones :
1. Apilar nombre (ingrese nombre por teclado, la primera letra debe estar en
mayúsculas) , al ingresar a esta opción ingresa los nombres repetidamente, sólo
dejará de ingresar nombres si ingresa un nombre vacío (Enter) para volver al menú.
2. Desapilar nombre
3. Salir
Antes de terminar debe mostrar todos los nombres de la pila en forma vertical (uno debajo de
otro) debe crear otro método para cumplir con este enunciado. El primer nombre debe ser el
último ingresado.
'''
from pilas import *

def menu():
    pilanombre = Pila()
    while True:
        print('''
     ----Menu----
1_Apilar Nombre.
2_Desapilar Nombre.
3_Salir
''')
        opcion = input('Ingrese una opcion: ')
        if opcion == '1':
            while True:
                nom = input(f'Ingrese un nombre o enter para salir: ').capitalize().strip()
                if len(nom) == 0:
                    break
                else:
                    pilanombre.apilar(nom)
        elif opcion == '2':
            pilanombre.desapilar()
        elif opcion == '3':
            pilanombre.imprimir_al_reves()
            print('Programa Terminado')
            break
        else:
            print('¡¡Opcion invalida!!')
        
menu()