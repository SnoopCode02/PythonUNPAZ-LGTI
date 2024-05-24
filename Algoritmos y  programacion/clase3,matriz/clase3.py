Matriz = []
f = int(input("Ingrese el numero de filas: "))
c = int(input("Ingrese el numero de columnas: "))
for i in range(f):
    Matriz.append([0]*c)

print(Matriz)

for i in Matriz:
    print(i)

for f in range(f):
    for c in range(c):
        Matriz[f][c] = int(input(f"Ingrese un numero para la posicion {f}-{c}: "))
        
for i in Matriz:
    print(i)

