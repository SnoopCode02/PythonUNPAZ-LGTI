'''
Utilizando un TDA Pila resuelva el siguiente juego.
El juego consiste en recordar 5 números apilados en una pila, el usuario deberá desapilar
uno a uno los números apilados,
desde el tope hasta la base, acertando el número que se encuentra en el tope.
Recuerde que la pila siempre desapila desde el tope.
A Programar
1. Apile 5 números al azar del 10 al 99 en un TDA Pila utilizando la función correcta de
random.
2. Muestre la pila y haga una pausa.
3. Realice un print() 100 veces utilice for. para limpiar la pantalla.
4. El Usuario tendrá 7 oportunidades en total para acertar los 5 números. Ingrese el número a
desapilar por teclado. Controle si uso todas las oportunidades o si ya acertó los 5 números.
Utilice contadores, ciclos y los métodos necesarios para desapilar, tenga en cuenta que
solo podrá desapilar si el número ingresado coincide con el número en el tope de la pila.
5. Al acertar los 5 números o al usar todas las oportunidades deberá controlar si el usuario
gano o perdio el juego.
Gana si la pila queda sin elementos.
Pierde si pasados las 7 oportunidades todavía quedan elementos
'''
from pilas import *
from random import randint
def es_entero_positivo(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
            return int(numero)
            break
        except ValueError:
            print('¡Por favor ingrese un numero entero positivo!')
            
def apilar_numeros(lista):
    num_list = lista
    for i in range(5):
        num = randint(10, 99)
        num_list.apilar(num)
def mostrar_numeros(lista):
    num_lista = lista
    print('''
¡Bienvenidoo!
Este es un juego divertido debes desapilar de arriba a abajo los numeros.
Memorice el orden, ¡¡asi que preste atencion!!
''')
    input('Presione enter para continuar.')
    num_lista.imprimir_al_reves()
    input('Presione enter para continuar.')
    for i in range(100):
        print()
        
def juego(lista):
    num_list = lista
    cont_fallos = 0
    while True:
        if cont_fallos == 7:
            print('Lo siento usted a perdido :(')
            break
        elif num_list.vacia():
            print('¡¡A GANADO!!, Lo has echo genial.')
            break
        
        num = es_entero_positivo('Ingrese el numero de la parte superior de la fila: ')
        if num_list.comparar(num):
            print(f'Acerto {num} Desapilado')
            num_list.desapilar()
        else:
            cont_fallos += 1
            print(f'Ups a fallado. Contador de fallos: {cont_fallos}')

def main():
    numeros = Pila()
    apilar_numeros(numeros)
    mostrar_numeros(numeros)
    juego(numeros)
main()








