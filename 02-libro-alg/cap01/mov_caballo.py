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

print(mov_caballo[0])
for m in mov_caballo:
    print(m)

def cant_movimientos(casilla_inicial, cant_mov_ini, mov_caballo, cant=0) -> int:
    if cant_mov_ini == 0 or casilla_inicial == 5:
        cant += 1
        return cant
    for i in mov_caballo[casilla_inicial]:
        cant_movimientos(i, cant_mov_ini - 1, mov_caballo, cant)
    
    cant += 1
    return cant

cant = 0
for i in range(10):
    cant += cant_movimientos(i, 1, mov_caballo)

print(cant)