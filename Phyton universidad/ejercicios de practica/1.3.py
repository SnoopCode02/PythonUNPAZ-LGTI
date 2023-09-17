PESO_POR_PAYASO=112
PESO_POR_MUNIECA=75
payasos=int(input("Ingrese la cantidad de payasos vendidos: "))
muniecas=int(input("Ingrese la cantidad de muñecas vendidas: "))
peso_total=PESO_POR_PAYASO*payasos+PESO_POR_MUNIECA*muniecas
print("El peso total es {peso} KG".format(peso=peso_total))