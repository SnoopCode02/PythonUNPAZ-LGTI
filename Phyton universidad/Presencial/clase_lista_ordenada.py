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
        
class ListaOrdenada:
    
    def __init__(self):
        self.cabeza = None
        
    def estaVacia(self):
        return self.cabeza == None
        
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
                
    def tamano(self):
        actual = self.cabeza
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.obtenerSiguiente()
        return contador
                
    def buscar(self, item):
        actual = self.cabeza
        encontrado = False
        detenerse = False
        while actual != None and not encontrado and not detenerse:
            if actual.obtenerDato() == item:
                detenerse = True
            else:
                actual = actual.obtenerSiguiente()
        return encontrado
    
    def agregar(self,item):
        actual = self.cabeza
        previo = None
        detenerse = False
        while actual != None and not detenerse:
            if actual.obtenerDato() > item:
                detenerse = True
            else:
                previo = actual
                actual = actual.obtenerSiguiente()
        temp = Nodo(item)
        if previo == None:
            temp.asignarSiguiente(self.cabeza)
            self.cabeza = temp
        else:
            temp.asignarSiguiente(actual)
            previo.asignarSiguiente(temp)
    def ver(self):
        print('Cabeza', end = '->')
        if self.estaVacia:
            
            actual = self.cabeza
            while actual != None:
                print(actual.dato, end = '->')
                actual = actual.obtenerSiguiente()
        print("None")
        
milista = ListaOrdenada()

milista.ver()
milista.agregar("A")
milista.agregar("Z")
milista.agregar("B")
milista.agregar("J")

milista.ver()

print("Remover B")
milista.remover("B")

print("Buscamos z", milista.buscar('Z'))

print("El tamaño es: ", milista.tamano())
milista.ver()

milista.agregar("M")

milista.ver()