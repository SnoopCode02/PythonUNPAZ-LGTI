
ruta = r'D:\algoritmo\archivo.txt'

def getAll():
    global ruta
    with open(ruta,'r') as archivo:
        for linea in archivo:
            print(linea.strip())

def getbyID(codigo):
    with open(ruta, 'r') as archivo:
        for linea in archivo:
            data = linea.split(',')
            if data[0] == codigo:
                return linea
        return None

def cargar_cliente(cliente):
    linea =  f"{cliente.IdC},{cliente.Nombre},{cliente.Apellido}, {cliente.Telefono}, {cliente.Direccion} \n"
    with open(ruta,'a') as archivo:
        archivo.write(linea)

def update(cliente):
    newline = F'{cliente.idC}, {cliente.Nombre}, {cliente.apellido}, {cliente.Telefono}, {cliente.Direccion}'
    posnuevalinea = pos
    with open(ruta, 'r') as archivo:
        lineas = archivo.readlines()
        for pos, item in enumerate(lineas,1):
            data = item.strip().split(',')
            if (data[0] == cliente.codigo):
                posnuevalinea = pos
                break
    if posnuevalinea > 0:
        lineas[posnuevalinea-1] = newline + '\n'
        with open(ruta, 'w') as archivo:
            archivo.writelines(lineas)
        

