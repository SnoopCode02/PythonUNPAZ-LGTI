import archivo
import model2

#leer archivo
archivo.listArchivo()


# crear un nuevo cliente
cliente = model2.Cliente('2','Ricardo', 'direcc 232', '22')
#archivo.agregarCliente(cliente)
#archivo.listArchivo()


# buscar un nuevo cliente 
codigo = '20'

clienteBusqueda = archivo.getCliente(codigo)
print(clienteBusqueda)
print(clienteBusqueda if clienteBusqueda is not None else 'El cliente no existe')



#update cliente 
#archivo.update(cliente)
#archivo.listArchivo()






