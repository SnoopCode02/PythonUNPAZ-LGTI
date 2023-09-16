'''crear la indexacion
crear buscar todos los repetidos y su posicion'''
class Nodo:
    def __init__(self, datoInicial):
        self.dato = datoInicial
        self.siguiente = None
        
    def obtenerDato(self):
        return self.dato
    
    def obtenerSiguiente(self):
        return self.siguiente
    
    def asignarSiguiente(self,nuevosiguientes):
        self.siguiente = nuevosiguientes
        
        
class ListaNoOrdenada:
    
    def __init__(self):
        self.cabeza = None
        
    def estaVacia(self):
        return self.cabeza == None
    
    def agregar(self,item):
        temp = Nodo(item)
        temp.asignarSiguiente(self.cabeza)
        self.cabeza = temp
        
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.obtenerSiguiente()
        return contador
    
    def buscar(self,item):
        actual = self.cabeza
        encontrado = False
        while actual != None and not encontrado:
            if actual.obtenerdato() == item:
                encontrado = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado
    
    def remover(self, item):
        actual = self.cabeza
        previo = None
        encontrado = False
        while not encontrado and actual != None:
            if actual.obtenerDato() == item:
                encontrado = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        if actual != None:
            if previo == None:
                self.cabeza = actual.obtenerSiguiente()
            else:
                previo.asignarSiguiente(actual.obtenerSiguiente())
        else:
            (f'El dato: {item} no se encuentra')
    
    def ver(self):
        print('Cabeza', end = '->')
        if not self.estaVacia:
            
            actual = self.cabeza
            while actual != None:
                print(actual.dato, end = '->')
                actual = actual.obtenerSiguiente()
        print("None")
    
    '''def anexar(self, item):
        final = False
        referencia = self.cabeza
        while not final:
            referencia = referencia.obtenersiguiente()
            if referencia == None:
                agregar(self.item)
                final = True'''
    def anexar(self,item):
        temp = nodo(item)
        actual = self.cabeza
        previo = None
        while actual != none:
            
milista = ListaNoOrdenada()

milista.ver()

milista.agregar(10)
milista.agregar(20)
milista.agregar(100)
milista.anexar(30)
milista.ver()

print(f'\nTamaño: {milista.tamano()}\n')

#borramos el elemento 100
print(milista.remover(100))
print(milista.remover(40))


milista.ver()

