import random
"""

"""
def isbisiesto(a):
    es = a%4 == 0 and a%100 != 0 or a%400 == 0
    return es

def obter_cantidad_diass_del_mes(m,anio):
    cantidad = 31
    if m in (4,6,9,11):
        cantidad= 30
    elif m == 2:
        if isbisiesto(anio):
            cantidad = 29
        else:
            cantidad = 28
    return cantidad
    
    
def obtener_fecha_random(anio):
    m = random.randint(1,12)
    cantidad_dias = obter_cantidad_diass_del_mes(m,anio)
    d = random.randint(1,cantidad_dias)
    return (anio*10000) + (m*100) + d #AAAAMMDD


def el_anio(aaaammdd):
    """
    Retorna el año de una fecha
    
    AAAA <== |MMDD
    """
    return aaaammdd//10000 #AAAA <== |MMDD

def el_mes(aaaammdd):
    return aaaammdd%100 #AAAAMM| ==> DD

def el_dia(aaaammdd):
    return (aaaammdd//100)%100 #AAAA| ==> MM <==|DD

def str_fecha(aaaammdd):
    anio = el_anio(aaaammdd)
    dia = el_dia(aaaammdd)
    mes = el_mes(aaaammdd)
    return f"{dia:02}/{mes:02}/{anio:04}"


"""
PROGRAMA PRINCIPAL
"""
def main():
    fecha = obtener_fecha_random(2023) #AAAAMMDD
    
    print(str_fecha(fecha))


main() # LLAMO A FUNCION PRINCIPAL







