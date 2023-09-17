## Ejercicio 048

### Escribir un programa que permita realizar varias operaciones matemáticas ingresando un caracter por cada una la operación a realizar (‘+’, ‘-’, ‘*’, ‘/’, ‘F’) y dos números enteros en el caso que no haya elegido ‘F’. La computadora debe mostrar el resultado para la operación ingresada. Considerar que no se puede dividir por cero. Cuando la operación ingresada sea ‘F’ nos indicará que no se desean calcular más operaciones.
operacion = ""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

while operacion != "F":
    operacion = input("Ingrese una operacion <<<'+', '-', '*', '/' o 'F' si no quiere mas operaciones>>>: ").upper()

    if operacion == "+" or operacion=="-" or operacion=="*" or operacion=="/" or operacion=="F":
        if operacion == "+":
            print(f"La operacion ingresada es la suma de: {num1} + {num2} = {num1+num2}")
        elif operacion == "-":
            print(f"La operacion ingresada es la suma de: {num1} - {num2} = {num1-num2}")
        elif operacion == "*":
            print(f"La operacion ingresada es la suma de: {num1} * {num2} = {num1*num2}")
        elif operacion == "/":
            if num2 != 0:
                print(f"La operacion ingresada es la suma de: {num1} / {num2} = {num1/num2}")
            else:
                print("La division por 0 no esta definida, por favor cambie el segundo numero.")
        else:
            print("Gracias por utilizar el programa.")
    else:
        print("La opcion no es correcta.")





