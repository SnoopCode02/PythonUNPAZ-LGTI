class Cola:
    
    def __init__(self):
        self.clientes = []
        
    def encolar(self, x):
        self.clientes.append(x)
        print(f'Cliente {x} agregado (encolado), cola actualizada: {self.clientes}')
        
    def es_vacia(self):       
        return self.clientes == []
    
    def desencolar(self):
        
        if self.es_vacia():
            print(f'La cola esta vacia no hay mas clientes')
        else:
            print(f'\nClientes {self.clientes.pop(0)} atendido(desencolado), cola actualizada: {self.clientes}')
    
    def mostrar(self):
        print(f'\nTurnos {self.clientes}')
    
        