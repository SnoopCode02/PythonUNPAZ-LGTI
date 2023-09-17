## Ejercicio 036

### Escribir un programa que permita ingresar dos números enteros y la operación a realizar('+', '-', '*', '/'). Debe mostrarse el resultado para la operación ingresada. Considerar que no se puede dividir por cero (en ese caso mostrar el texto 'ERROR').

num = ""
num2 = ""

def isnum(s):
    try:
        int(s)
    except:
        ValueError
        return False
    else:
        return True

LIM_INF = 1
LIM_SUP = 4
flag = False
flag2 = False
flag3 = False
operacion = ""
resultado = 0
que_operacion = None
while not flag:
    num = input("Ingrese el primer numero: ")
    num2 = input("Ingrese el segundo numero: ")
    if isnum(num) and isnum(num2):
        flag = not flag
        num = int(num)
        num2 = int(num2)
        while not flag2:
            que_operacion = input("¿Que operacion desea hacer?\n1- Para suma '+'\n2- Para resta '-'\n3- Para multiplicacion '*'\n4- Para division. '/'\nOpcion:")
            if isnum(que_operacion):
                que_operacion = int(que_operacion)
                if LIM_INF <= que_operacion <= LIM_SUP:
                    flag2 = not flag2
                else:
                    print("La opcion ingresada no es valida por favor vuelva a intentarlo.")
            else:
                print("La opcion ingresada no es valida por favor vuelva a intentarlo.")
    else:
        print("Por favor ingrese numeros")

if que_operacion == 1:
    operacion = "Suma"
    resultado = num + num2
    print(f"La operacion es una: {operacion} y el resultado es: {resultado}")
elif que_operacion == 2:
    operacion = "Resta"
    resultado = num - num2
    print(f"La operacion es una: {operacion} y el resultado es: {resultado}")
elif que_operacion == 3:
    operacion = "Multiplicacion"
    resultado = num * num2
    print(f"La operacion es una: {operacion} y el resultado es: {resultado}")
elif que_operacion == 4:
    if num2 != 0:
        operacion = "Division"
        resultado = round((num / num2),2)
        print(f"La operacion es una: {operacion} y el resultado es: {resultado}")
    else:
        print("La division por 0 es indefinida, por favor cambie el segundo numero.") 
 
 



