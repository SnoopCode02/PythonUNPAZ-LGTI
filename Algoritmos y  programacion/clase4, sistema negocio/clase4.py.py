class Persona:
    def __init__(self, nombre,apellido,cursa):
        self.nombre = nombre
        self.apellido = apellido 
        self.cursa = cursa
    def toString(self):
        print(self.nombre, '', self.apellido)
        return f'{self.nombre} {self.apellido} {self.cursa}'
    def cambiarEstado(self):
        self.cursa = False


listaPersona = []
p1 = Persona('alex','ayala',True)
p2 = Persona('romulo', 'ojo', True)
p3 = Persona('lumi', 'perez', True) 

print(p1.nombre)
print(p1.apellido)

p1.toString()


listaPersona.append(p1)




"""
El cliente ha solicitado un sistema para gestionar las ventas de su negocio,
que incluye 10 productos con un stock inicial. Los datos que desea almacenar sobre cada producto son:
ID del producto, Nombre o Descripción, Cantidad en stock y Precio. Además, desea registrar la información de ventas,
que incluye: ID de la venta, ID del producto, Nombre del producto, Descripción del producto 
Cantidad vendida, Precio unitario, Total de la venta, El cliente también solicita los siguientes informes:
Listar todas las ventas. Listar las ventas ordenadas de mayor a menor. Buscar las ventas de un producto específico. 
Realizar un cierre de caja que incluya: Suma total de todas las ventas. Cantidad total de productos vendidos. 
Para cumplir con los requerimientos del cliente, necesitaremos desarrollar un sistema que permita la gestión de productos,
ventas y generación de informes según lo solicitado.

"""

