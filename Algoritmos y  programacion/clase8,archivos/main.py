import archivo
import Model
archivo.getAll()
archivo.getbyID(3)

while True:
    try:
        for i in range(1):
            codigo = input('Ingrese un codigo: ')
            nombre = input('Ingrese el nombre del cliente: ')
            apellido = input('Ingrese un apellido: ')
            telefono = input('Ingrese su telefono: ')
            direccion = input('Ingrese su direccion: ')
            c1 = Model.Cliente(codigo, nombre, apellido, telefono, direccion)
        break
    except Exception: 
        print('ups algo paso!')

archivo.cargar_cliente(c1)

archivo.getbyID(3)