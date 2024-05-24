class Cola:
    
    def __init__(self):
        self.objeto = []
        
    def encolar(self, x):
        self.objeto.append(x)
        print(f'Paciente {x} agregado (encolado), cola actualizada: {self.objeto}')
        
    def es_vacia(self):       
        return self.objeto == []
    
    def desencolar(self,item):
        if self.es_vacia():
            print(f'La cola esta vacia no hay mas Pacientes')
        else:
            print(f'\nPaciente {item} atendido(desencolado), cola actualizada: {self.objeto}')
            self.objeto.remove(item)
    def mostrar(self):
        print(f'\nTurnos {self.objeto}')
    
        