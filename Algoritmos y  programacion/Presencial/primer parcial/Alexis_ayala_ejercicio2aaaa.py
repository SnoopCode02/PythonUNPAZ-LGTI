from ListaORDENADA_parcial import *
from tda_parcial import *

def cargar_lista(num_list, str_list):
   for i in range(1,10):
       num_list.agregar(i)
#Las palabras se ordenaran con respecto al abecedario, la A seria primero, segundo B, tercero C...etc
    str_list.agregar('CINCO')
    str_list.agregar('CUATRO')
    str_list.agregar('SEIS')
    str_list.agregar('NUEVE')
    str_list.agregar('DOS')
    str_list.agregar('CERO')
    str_list.agregar('TRES')
    str_list.agregar('SIETE')
    str_list.agregar('UNO')
    str_list.agregar('OCHO')
def combinar(num_list, str_list, comb_list):
    for i in str_list:
        if i is int:
            comb_list.encolar(str(i))
        else:
            comb_list.encolar(i)
    comb_list.mostrar

def 
def main():
    cola_combinada = Cola()
    lista_num = ListaOrdenada()
    lista_str = ListaOrdenada()
    cargar_lista(lista_num, lista_str)
    combinar(lista_num, lista_str, cola_combinada)
    
main()