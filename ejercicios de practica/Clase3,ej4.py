PAYASOS = 112
MUÑECAS = 75
cant_de_payasos = float(input("¿Cuantos payasos lleva la caja? "))
cant_de_muñecas = float(input("¿cuantas muñecas lleva la caja? "))
peso_de_la_caja = ((cant_de_payasos * PAYASOS)+(cant_de_muñecas * MUÑECAS))
print("El peso final de tu caja es: %.2fg" %peso_de_la_caja)