from globales import IMAGENES, PALABRAS
from random import randint


def crear_palabra_oculta(palabra):
    oculta = []
    for _ in palabra:
        oculta.append("_")
    return oculta


palabra_a_adivinar = list(PALABRAS[randint(0, len(PALABRAS) - 1)].upper())
palabra_oculta = crear_palabra_oculta(palabra_a_adivinar)
intentos = len(IMAGENES) - 1


def indexar_al_reves(lista, indice):
    return lista[len(lista) - 1 - indice]


def mostrar_palabra_oculta():
    global palabra_oculta
    str = ""
    for letra in palabra_oculta:
        str += f"{letra} "
    print(str)


def intentar_con_letra(letra):
    global palabra_oculta
    resultado_intento = False
    for i in range(len(palabra_a_adivinar)):
        if palabra_a_adivinar[i] == letra:
            resultado_intento = True
            palabra_oculta[i] = letra
    return resultado_intento


def intentar_con_palabra(palabra):
    global palabra_oculta
    resultado_intento = False
    if palabra_a_adivinar == list(palabra):
        resultado_intento = True
        palabra_oculta = palabra_a_adivinar
    return resultado_intento


def ganaste():
    return palabra_oculta == palabra_a_adivinar


def no_hay_mas_intentos():
    return intentos <= 0


def se_sigue_jugando():
    return not ganaste() and not no_hay_mas_intentos()


while se_sigue_jugando():
    print(indexar_al_reves(IMAGENES, intentos))
    print(f"Intentos disponibles: {intentos}")
    mostrar_palabra_oculta()
    print("Ingrese una letra o la palabra: ")
    letra_o_palabra = input().upper()
    intento_exitoso = False
    if len(letra_o_palabra) == 1:
        intento_exitoso = intentar_con_letra(letra_o_palabra)
    elif len(letra_o_palabra) > 1:
        intento_exitoso = intentar_con_palabra(letra_o_palabra)
    if not intento_exitoso:
        intentos -= 1
        print("Ups! intenta de nuevo")
    else:
        print("Bien, acertaste!")
if ganaste():
    print("Felicidades, ganaste!")
elif no_hay_mas_intentos():
    print("Lo siento se termino el juego!")
