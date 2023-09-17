FILAS = 9
COLUMNAS = 9
PFILA = 0
PCOLU = 0
UFILA = FILAS - 1
UCOLU = FILAS -1
MFILA = FILAS//2
MCOLU = FILAS//2

print("letra O")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == 0 or f == FILAS-1 or c== 0 or c == COLUMNAS-1:
            print('*',end="")
        else:
            print(' ',end='')
            
    print()
    
    
print("letra L")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == FILAS-1 or c== 0:
            print('*',end="")
        else:
            print(' ',end='')
            
    print()
    
    
print("letra S")

for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == PFILA or f == UFILA or f == MFILA or (f>=MFILA and c == UCOLU) or \
            (f<= MFILA and c == PCOLU):
            print('*',end="")
        else:
            print(' ',end='')
            
    print()    
print("letra S")   
    
for f in range(FILAS):
    for c in range(COLUMNAS):
        #print(f"({f},{c})")
        if f == c :
            print('*',end="")
        else:
            print(' ',end='')
            
    print() 