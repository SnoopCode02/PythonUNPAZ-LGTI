'''
3. Resuelva con un TDA COLA:
Estamos en el mostrador de una clínica y nos encargamos de otorgar los turnos/números y
también de llamar a los pacientes para ser atendidos.
Tener en cuenta que:
dar turno = encolar
llamar al paciente = desencolar
Se pide:
● Cree un objeto de la clase Cola llamado, Turno
● Dar turnos a 10 pacientes empezando por el número cero
● Llame, a los primeros 3.
● Cuando está por llamar a los pacientes 4 y 5 se da cuenta de que estos no están,
¿como hace para llamar al paciente 6 ?
● Llame al paciente 6
● Vuelva a otorgar 3 números más, a otros 3 pacientes (Recuerde seguir el orden de
llamada).
● Muestre la cola de turnos actualizada.
'''
from colas import *

def dar_turnos(turno_list):
    for i in range(10):
        turno_list.encolar(i)
    
    if desencolar(turno_list):
        for i in range(10,13):
            turno_list.encolar(i)
        
def desencolar(turno_list):
    for i in range(7):
        if i == 4:
            print(f'El paciente 4 no se encuentra, cuando vuelva sera atendido!')
        elif i == 5:
            print(f'El paciente 5 no se encuentra, cuando vuelva sera atendido')
        else:
            turno_list.desencolar(i)
    return True
    
def main():
    turno_cola = Cola()
    dar_turnos(turno_cola)
main()