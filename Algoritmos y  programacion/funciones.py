def introducir_entero_valido(mensaje):
    while True:
        num = input(mensaje).strip()
        try:    
            num = int(num)
            return int(num)    
        except ValueError:
            print(f"El numero: {num} no es un entero, presione enter para continuar.")
            input()