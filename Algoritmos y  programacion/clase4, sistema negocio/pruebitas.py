def es_entero_positivo(sTr):
    while True:
        numero = input(sTr).strip()
        try:
            int(numero)
            break
        except ValueError:
            print('¡Por favor ingrese un numero entero!')
        numero = int(numero)
        while True:
            if numero >= 0:
                return int(numero)
            else:
                print('¡Por favor ingrese un numero entero positivo!')
            
            
es_entero_positivo('holjsiaho')