from ListaORDENADA_parcial import *
from tda_parcial import *
cola_combinada = Cola()
lista_combinada = ListaOrdenada()
combinados = ['CUATRO', 2, 3, 'CINCO', 'SEIS', 4, 'NUEVE', 'DOS', 'CERO', 'TRES', 6, 'SIETE', 9, 5, 'UNO', 'OCHO', 1, 7, 8]
for i in combinados:
    x = str(i)
    cola_combinada.encolar(x)

for i in range(19):
    num = cola_combinada.desencolar(i)
    lista_combinada.agregar(num)
lista_combinada.ver()
print('Las letras se ordenan respecto a su posicion en el abecedario')
'''
Lo que cambie de la funcion
def desencolar(self,index):      
        if self.es_vacia():
            print("La cola está vacía")
        else:
            return self.lista_cola[index]           
    def es_vacia(self):
        return self.lista_cola == []
'''
'''
El nuevo metodo es para buscar un item segun su indice.
'''
ejemplo = lista_combinada.metodo_nuevo(4)
print(ejemplo)
ejemplo2 = lista_combinada.metodo_nuevo(30)
print(ejemplo2)
