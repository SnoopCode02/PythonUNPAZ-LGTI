
class Pila:
    #Definimos el constructor
    def __init__(self):
        #inicializamos una 'Pila vacia', el elemento contenedor 
        self.lista = []
    
    def apilar(self,item):
        self.lista.append(item)
        print(f'\nElemento {item} apilado, lista actualizada: {self.lista}')

    def vacia(self):
        if len(self.lista) == 0:
            return True
        else:
            return False
        
    def desapilar(self):
        if self.vacia():
            print(f'\nNo se puede desapilar la lista esta vacia')
        else:
            self.lista.pop(-1)
    
    def tamanio(self):
        print(f'\nLa pila tiene {len(self.lista)} elementos')
        return len(self.lista)
    
    def limpiar(self):
        self.lista.clear()
        print('\nLista vaciada')
        
    def imprimir_al_reves(self):
        for i in self.lista[::-1]:
           print(f'[{i}]')
           
    def imprimir(self):
        for i in self.lista:
           print(f'[{i}]')
           
    def comparar(self,item):
        for i in range(len(self.lista)):
            if self.lista[i-1] == item:
                return True
            else:
                return False
        