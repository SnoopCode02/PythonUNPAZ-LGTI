
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
            print(f'\nElemento {self.lista.pop()} desapilado, lista actualizada: {self.lista}')
    
    def tamanio(self):
        print(f'\nLa pila tiene {len(self.lista)} elementos')
        return len(self.lista)
    
    def limpiar(self):
        self.lista.clear()
        print('\nLista vaciada')
pila_letra = Pila()       
for i in range(10):
    letra = input(f'Ingrese la {i+1}° letra: ')
    pila_letra.apilar(letra)
    
for i in range(pila_letra.tamanio()):
    pila_letra.desapilar()