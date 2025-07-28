def cant_mov(casilla, mov):
    total = 0
    mov_caballo = ((4,6),    # 0
                    (6,8),   # 1
                    (7,9),   # 2
                    (4,8),   # 3
                    (0,9,3), # 4
                    None,    # 5
                    (1,7,0), # 6
                    (2,6),   # 7
                    (1,3),   # 8
                    (2,4))   # 9
    if casilla == 5:
        return 0

    if mov == 0:
        return 1
    
    for c in mov_caballo[casilla]:
        total += cant_mov(c, mov - 1)
    return total

print(cant_mov(1,2))
    
def cant_mov_tablero(mov):
    total_mov_tablero = 0
    for i in range(10):
        total_mov_tablero += cant_mov(i,mov)
    return total_mov_tablero

print("Cantidad de movimientos".ljust(25) + "Posibilidades válidas".ljust(25))
for i in range(19):
    print(f"  {i}".ljust(25) +  f"  {cant_mov_tablero(i)}".ljust(25))


