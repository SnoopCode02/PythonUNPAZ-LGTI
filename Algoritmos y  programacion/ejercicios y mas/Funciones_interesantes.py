'''Funciones interesantes de Alexis Ayala'''
def es_entero_positivo(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
            break
        except ValueError:
            print('¡Por favor ingrese un numero entero positivo!')
    int(numero)
    while True:
        if numero >= 0:
            return int(numero)
        else:
            print('¡Por favor ingrese un numero entero positivo!')
            
def es_entero_Negativo(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
        except ValueError:
            print('¡Por favor ingrese un numero entero negativo!')
        if numero <= 0:
            break
        else:
            print('¡Por favor ingrese un numero entero negativo!')
    
            
def es_entero(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
            return int(numero)
        except ValueError:
            print('¡Por favor ingrese un numero entero!')

def es_Flotante(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            float(numero)
            return float(numero)
        except ValueError:
            print('¡Por favor ingrese un numero entero!')            
