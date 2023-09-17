"""Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros),
 calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla 
la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal 
calculado redondeado con dos decimales."""
Peso = float(input("Digame su peso en Kg: "))
altura = float(input("Digame su altura en Mts: "))
altura_al_cuadrado = altura ** 2
imc = (Peso/altura_al_cuadrado)
print("Tu indice de masa corporal es: %.2f" %imc)