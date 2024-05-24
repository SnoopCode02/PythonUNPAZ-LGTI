class Producto:
    def __init__(self, iD, nombre, descripcion,  stock, precio):
        self.id = iD
        self.nombre = nombre
        self.stock = stock
        self.precio = precio
        self.descripcion = descripcion
        
    def cambiar_stock(self, stock):
        self.stock = stock

class Ventas:
    def __init__(self, iD_venta, iDprodu , nombre, cantidad, precio_tot):
        self.iD_venta = iD_venta
        self.iDprodu = iDprodu
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio_tot = precio_tot
        
        

def cargar_productos(productos):
    productos_loc = productos
    cant = int(input('¿Cuantos productos desea cargar?: '))
    for i in range(cant):
        nomb_producto = input('Ingrese el Nombre del producto: ').capitalize()
        descripcion_produ = input('Ingrese una descripcion para el producto').capitalize()
        cod_id = es_entero('Ingrese un ID numerico de 4 digitos para el producto: ')
        cantidad = int(input('Ingrese la cantidad de stock: '))
        precio = float(input('Ingrese el precio del producto: '))
        p = Producto(cod_id, nomb_producto, descripcion_produ, cantidad, precio)
        productos_loc.append(p)



def cargar_info_ventas(productos, ventas_loc):
    flag = False
    ventas_loc = ventas_loc
    productos_loc = productos
    while not flag:
        cant = int(input('¿Cuantas ventas desea cargar?: '))
        for i in range(cant):
            cod_id = len(ventas_loc) + 1
            nomb_venta = input('Ingrese el Nombre del producto que quiere comprar: ').upper()
            descripcion_produ = input('Ingrese la descripcion del producto que quiere comprar: ')
            cod_id_producto = 0
            precio = 0
            cantidad = es_entero('Ingrese la cantidad que quiere comprar: ')
            precio_total = cantidad + precio
            v = Ventas(cod_id, nomb_venta, cantidad, precio_total)
            ventas_loc.append(v)
        while True:
            op = input("Desea ingresar una venta mas? 'S' para si, 'N' para no: ").upper()
            if op == 'S':
                cant = input('¿Cuantas?: ')
                break
            elif op == 'N':
                flag = True
                break
            else:
                print('Por favor elija una opcion correcta!!')

def listar_ventas():
    pass

def listar_vent_mayor_A_menor():
    pass

def cierre_de_caja():
    pass

def es_entero(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
            return int(numero)
        except ValueError:
            print('¡Por favor ingrese un numero entero!')

def es_Flotante(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            float(numero)
            return float(numero)
        except ValueError:
            print('¡Por favor ingrese un numero entero!')
