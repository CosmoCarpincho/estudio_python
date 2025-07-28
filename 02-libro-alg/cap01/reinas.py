def imprimir_matriz(matriz):
    for fila in matriz:
        linea = ""
        for casilla in fila:
            linea += f"{str(casilla):>3}" # :>3 ancho fijo de 3 alineado a la derecha
        print(linea)

# 0 que no esta amenazada
# 1 que esta amenazada u ocupada
def crear_matriz(num_reinas):
    return [['0' for _ in range(num_reinas)] for _ in range(num_reinas)]

def amenaza_reina(matriz, pos_i, pos_j, bloq=1, reina='r'):
    long = len(matriz[0])
    # horizontal
    for j in range(long):
        matriz[pos_i][j] = bloq
    # vertical
    for i in range(long):
        matriz[i][pos_j] = bloq
    
    # diagonal sup->inf
    # inf    
    i = pos_i
    j = pos_j
    while i < long and j < long:
        matriz[i][j] = bloq
        i += 1
        j += 1
    # sup
    i = pos_i
    j = pos_j
    while i >= 0 and j >= 0:
        matriz[i][j] = bloq
        i -= 1
        j -= 1
    
    # diagonal inf->sup
    #inf
    i = pos_i
    j = pos_j
    while i < long and j >= 0:
        matriz[i][j] = bloq
        i += 1
        j -= 1

    #sup
    i = pos_i
    j = pos_j
    while i >= 0 and j < long:
        matriz[i][j] = bloq
        i -= 1
        j += 1
    
    matriz[pos_i][pos_j] = reina

m = crear_matriz(10)
for fila in m:
    print(fila)

print("====")
amenaza_reina(m,4,4)
imprimir_matriz(m)

print("====")
amenaza_reina(m,0,1,2)
imprimir_matriz(m)


# recorrer la matriz y si esta libre poner reina
def poner_reina(matriz, ultima_ubicacion=None) -> tuple:
    for i, fila in enumerate(matriz):
        for j, casilla in enumerate(fila):
            if casilla == 0 and (ultima_ubicacion == None or (i,j) != ultima_ubicacion):
                matriz[i][j] = 'r2'
                return (i, j)

print("====")
poner_reina(m)
imprimir_matriz(m)
