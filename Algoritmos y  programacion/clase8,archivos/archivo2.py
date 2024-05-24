import model2
ruta = r'C:\JM\UNPAZ\2024\Algoritmo\archivo.txt'


def listArchivo():
    global ruta
    with open(ruta, 'r')  as archivo :
        for linea in archivo:
            print(linea.strip())




def agregarCliente(cliente):
    lineaNueva = f"{cliente.codigo}, {cliente.nombre},{cliente.direccion},{cliente.saldo}"
    with open(ruta, 'a') as archivo:
        archivo.write(lineaNueva)


def getCliente(codigo):
    with open(ruta, 'r') as archivo:
        for item in archivo:
            data = item.split(',')
            if data[0]== codigo:
                return item
        return None


def update(cliente):
     lineaNueva = f"{cliente.codigo}, {cliente.nombre},{cliente.direccion},{cliente.saldo}"
     posNuevaLinea = 0
     with open(ruta, 'r') as archivo:
         lineas =  archivo.readlines()
         for pos, item in  enumerate(lineas,1):
             data = item.strip().split(',')
             if(data[0] == cliente.codigo):
                 posNuevaLinea =  pos
                 break
     if posNuevaLinea > 0:
          lineas[posNuevaLinea -1] = lineaNueva + '\n'
          with  open(ruta, 'w') as archivo:
              archivo.writelines(lineas)

    
    

     
             