## Ejercicio 049

### Escribir un programa que permita validar una opción ingresada. Se le preguntará al usuario si desea continuar con alguna operación de la forma "¿Deseás continuar? [S/N]". Se espera que el usuario ingrese una 'S' o una 'N' (incluir las minúsculas). La opción debe ser ingresada tanto como sea necesario hasta que quede comprendida dentro de las posibilidades esperadas.


desea = ""
while desea != "N":
  desea = input("Desea continuar? [S/N]: ").upper()
  if desea == "S" or desea == "N":
    desea = desea
  else:
    print("Opcion ingresada no es valida.")