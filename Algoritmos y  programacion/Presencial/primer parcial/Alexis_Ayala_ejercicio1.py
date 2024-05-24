'''
El banco propio de la universidad " BUNPAZ " abre a las 10 AM y otorga 10 turnos
desde el número 0 al 9 todos los dias. Al banco posee 3 cajas A , B y C para atender estos clientes.

Ud debe realizar un programa que otorgue los números a cada cliente, estos esperan ser llamados,
por las cajas = ['A','B','C'] . Las cajas son asignadas aleatoriamente hasta terminar de atender a todos los clientes.

Haga uso de las funciones aleatorias.

Se le otorgarán los TDA correspondientes de Pila y Cola, estarán en un archivo llamado tda_parcial.py
este debe alojarse en la misma carpeta donde está ejecutando su programa.

recuerde usar from tda_parcial import *
'''
from tda_parcial import*
import random

def turnos(turno_list):
    for i in range(10):
        turno_list.encolar(i)
        print(f'Turno {i} Otorgado')

def atencion_al_cliente(turno_list):
    caja = ['A','B','C']
    print(f'\nSistema de atencion al cliente\n')
    for i in range(10):
        seleccion = random.choice(caja)
        print(f"Numero {i} Caja '{seleccion}'")
        

def main():
    turno_cola = Cola()
    turnos(turno_cola)
    atencion_al_cliente(turno_cola)

main()