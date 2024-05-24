import utilities
import librerias

productos = []
ventas = []

op = 0
op2 = 0
while op != 5:
    utilities.menuP()
    op = int(input('Ingrese una opcion: '))
    if op == 1:
        librerias.cargar_productos(productos)
    elif op == 2:
        librerias.cargar_info_ventas(productos, ventas)
    elif op == 3: 
        while op2 != 4:
            utilities.menuInfo()
            op2 = int(input('Ingrese una opcion: '))
            if op2 == 1:
                librerias.listar_ventas(ventas)
            elif op2 == 2:
                librerias.listar_vent_mayor_A_menor(ventas)
    elif op == 4:
        librerias.cierre_de_caja(ventas)
    elif op == 5:
        print('Gracias por utilizar el programa!!')
    else:
        print('Ingrese una opcion correcta')

